import tempfile
import unittest
from pathlib import Path

from mizoki_runtime import create_runtime


REPO_ROOT = Path(__file__).resolve().parents[1]


class BossRuntimeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.runtime = create_runtime(base_dir=REPO_ROOT, data_dir=Path(self.temp_dir.name))

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_expected_tools_are_registered(self) -> None:
        tool_names = {tool["name"] for tool in self.runtime.list_tools()}
        self.assertEqual(
            {
                "decision.explain_pipeline",
                "decision.recent_traces",
                "graphrag.query",
                "kg.describe_entity",
                "kg.list_neighbors",
                "skills.learn",
                "skills.list",
                "tools.list",
                "tools.register_alias",
            },
            tool_names,
        )

    def test_registered_tools_expose_complete_argument_schema(self) -> None:
        tools = {tool["name"]: tool for tool in self.runtime.list_tools()}
        schema = tools["graphrag.query"]["argument_schema"]
        self.assertEqual("object", schema["type"])
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(["query"], schema["required"])
        self.assertEqual("integer", schema["properties"]["top_k"]["type"])

    def test_alias_tool_registration_is_persisted_and_callable(self) -> None:
        registration = self.runtime.call_tool(
            "tools.register_alias",
            {
                "name": "graphrag.quick_query",
                "description": "Fast GraphRAG lookup for concise answers.",
                "target_tool": "graphrag.query",
                "default_arguments": {"top_k": 1},
                "tags": ["graphrag", "fast"],
            },
        )
        self.assertEqual("graphrag.quick_query", registration["result"]["tool"]["name"])

        execution = self.runtime.call_tool("graphrag.quick_query", {"query": "decision control plane"})
        self.assertEqual("graphrag.query", execution["resolved_tool"])
        self.assertEqual(1, execution["arguments"]["top_k"])
        self.assertTrue(execution["result"]["matches"])

    def test_alias_registration_rejects_invalid_default_arguments(self) -> None:
        with self.assertRaises(ValueError):
            self.runtime.call_tool(
                "tools.register_alias",
                {
                    "name": "graphrag.bad_alias",
                    "description": "Broken alias that should be rejected.",
                    "target_tool": "graphrag.query",
                    "default_arguments": {"top_k": "oops"},
                    "tags": ["graphrag"],
                },
            )

    def test_boss_can_learn_skills_and_route_to_preferred_tool(self) -> None:
        learned_skill = self.runtime.learn_skill(
            {
                "name": "dcp explainer",
                "description": "Prefer the pipeline explainer when users ask about the Decision Control Plane.",
                "trigger_phrases": ["decision control plane", "dcp"],
                "preferred_tools": ["decision.explain_pipeline"],
                "examples": ["Explain the decision control plane."],
            }
        )
        self.assertEqual("dcp explainer", learned_skill["name"])

        execution = self.runtime.execute("Explain the decision control plane and how it governs actions.")
        self.assertEqual("decision.explain_pipeline", execution["selection"]["tool_name"])
        self.assertGreaterEqual(execution["selection"]["confidence"], 0.45)
        self.assertEqual("decision.explain_pipeline", execution["execution"]["resolved_tool"])

    def test_boss_can_learn_skill_from_natural_language_request(self) -> None:
        execution = self.runtime.execute("Learn a new skill for decision control plane questions.")
        self.assertEqual("skills.learn", execution["selection"]["tool_name"])
        learned_skill = execution["execution"]["result"]["skill"]
        self.assertIn("decision.explain_pipeline", learned_skill["preferred_tools"])
        self.assertTrue(any("decision control plane" in phrase.lower() for phrase in learned_skill["trigger_phrases"]))

        follow_up = self.runtime.execute("Decision control plane questions")
        self.assertEqual("decision.explain_pipeline", follow_up["selection"]["tool_name"])

    def test_boss_records_decision_traces(self) -> None:
        self.runtime.execute("List the available tools.")
        traces = self.runtime.recent_traces(limit=3)
        self.assertEqual(1, len(traces))
        self.assertEqual("tools.list", traces[0]["selection"]["tool_name"])


if __name__ == "__main__":
    unittest.main()
