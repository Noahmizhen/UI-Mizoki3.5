"""Content data for MIZOKI3 static subpage generator."""

from __future__ import annotations

LENS_PAGES: dict[str, dict] = {
    "counsel": {
        "slug": "counsel",
        "title": "Counsel",
        "label": "LEGAL INTELLIGENCE",
        "tag": "Legal Intelligence",
        "meta_description": "Obligation mapped. Exposure quantified. Position verified — governed legal intelligence from MIZOKI3.",
        "hero_image": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1920&q=80&auto=format&fit=crop",
        "hero_aria": "Grand courthouse columns at dusk",
        "headline": "Obligation mapped. Exposure quantified. Position verified.",
        "hero_body": (
            "Counsel transforms the unstructured weight of contracts, correspondence, and litigation "
            "into a continuously updated decision landscape — mapping every obligation, detecting every "
            "contradiction, and scoring every pathway before action is taken."
        ),
        "capabilities_label": "CAPABILITIES",
        "capabilities_headline": "From raw legal complexity to governed intelligence.",
        "capabilities_intro": (
            "Counsel does not assist lawyers with research or drafting. It processes legal reality — "
            "contracts, correspondence, regulatory change, and dispute signals — into structured, causal, "
            "actionable intelligence the enterprise can govern and act on."
        ),
        "capabilities": [
            {
                "title": "Obligation Mapping",
                "body": (
                    "Every contract, amendment, and regulatory filing is decomposed into obligation nodes — "
                    "who owes what, to whom, under what conditions, with what deadlines. The graph tracks "
                    "obligations across entities, jurisdictions, and time."
                ),
            },
            {
                "title": "Contradiction & Exposure Detection",
                "body": (
                    "Counsel continuously scans for conflicts between obligations — a covenant in one agreement "
                    "that contradicts a commitment in another, a regulatory change that invalidates an existing "
                    "contract term. Contradictions surface before they become liabilities."
                ),
            },
            {
                "title": "Litigation Pathway Analysis",
                "body": (
                    "When disputes emerge, Counsel maps the decision tree of possible legal actions — scoring "
                    "each pathway by probability, cost, duration, and downstream business impact. The analysis "
                    "is causal, not correlational."
                ),
            },
        ],
        "cross_label": "CROSS-DOMAIN INTELLIGENCE",
        "cross_headline": "What Counsel learns, the entire system inherits.",
        "cross_body": (
            "Counsel doesn't operate in isolation. Every obligation it maps, every covenant it tracks, "
            "every risk it identifies flows into the shared knowledge graph — where Capital reads it as a "
            "financial constraint, Risk reads it as a compliance requirement, and Signal reads it as a "
            "boundary on marketing execution. One legal insight propagates across every decision the system makes."
        ),
        "cross_image": "https://images.unsplash.com/photo-1487958449943-2429d8be8626?w=1920&q=80&auto=format&fit=crop",
        "cross_aria": "Modern architectural interior suggesting interconnected corridors",
        "ingests": [
            "Contracts & amendments",
            "Litigation filings & discovery",
            "Negotiation transcripts",
            "Regulatory communications",
            "Correspondence & memoranda",
            "Fiduciary documentation",
            "Voice transcripts",
        ],
        "produces": [
            "Legal exposure maps",
            "Obligation propagation graphs",
            "Contradiction detection alerts",
            "Litigation pathway scores",
            "Negotiation leverage assessments",
            "Fiduciary deviation warnings",
            "Regulatory compliance verification",
        ],
        "cta_headline": "See Counsel map your obligations live.",
        "cta_subject": "MIZOKI3%20Counsel%20Briefing",
    },
    "signal": {
        "slug": "signal",
        "title": "Signal",
        "label": "MARKETING INTELLIGENCE",
        "tag": "Marketing Intelligence",
        "meta_description": "Correlation guesses. Causation governs — causal marketing intelligence from MIZOKI3.",
        "hero_image": "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?w=1920&q=80&auto=format&fit=crop",
        "hero_aria": "Aerial view of a city skyline at dusk with lights beginning to turn on",
        "headline": "Correlation guesses. Causation governs.",
        "hero_body": (
            "Signal replaces assumption-based marketing with causal autonomous execution — learning what "
            "actually moves customers, then steering spend, channel, and creative through the same governed "
            "pipeline the rest of the enterprise uses."
        ),
        "capabilities_label": "CAPABILITIES",
        "capabilities_headline": "From attribution guesswork to governed acquisition.",
        "capabilities_intro": (
            "Signal does not report last-click metrics or optimize in a silo. It traces what actually "
            "moves customers, then steers spend and creative through the same SRPVDAL pipeline and Decision "
            "Control Plane that govern every other enterprise action."
        ),
        "capabilities": [
            {
                "title": "Causal Attribution",
                "body": (
                    "Signal doesn't guess which touchpoint drove a conversion. It traces the causal chain — "
                    "what actually influenced the outcome, what was incidental, and what would have happened "
                    "if the touchpoint hadn't existed. Attribution built on counterfactual evidence, not "
                    "last-click correlation."
                ),
            },
            {
                "title": "Autonomous Bid Optimization",
                "body": (
                    "Media buying decisions flow through the SRPVDAL pipeline and the Decision Control Plane. "
                    "Every bid adjustment is causally justified, policy-compliant, and scored against simulated "
                    "alternatives before execution. No black-box automation — governed autonomy."
                ),
            },
            {
                "title": "Threshold-Aware Execution",
                "body": (
                    "Signal understands the activation thresholds and learning stability dynamics of "
                    "advertising platforms. It doesn't fight the algorithm — it works with the platform's "
                    "own optimization mechanics while maintaining causal oversight."
                ),
            },
        ],
        "cross_label": "CROSS-DOMAIN INTELLIGENCE",
        "cross_headline": "Marketing decisions bounded by legal reality and financial constraints.",
        "cross_body": (
            "A covenant tracked by Counsel becomes a spending constraint in Signal. A liquidity threshold "
            "monitored by Capital becomes a budget ceiling. Signal doesn't operate in a marketing silo — "
            "it inherits the enterprise's full legal and financial context through the shared knowledge graph."
        ),
        "cross_image": "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=1920&q=80&auto=format&fit=crop",
        "cross_aria": "Highway interchange at night with light trails suggesting flow",
        "cross_solid": True,
        "ingests": [
            "Meta advertising data",
            "Google advertising data",
            "CRM systems",
            "Customer journey telemetry",
            "Web analytics",
            "Conversion events",
            "Engagement signals",
            "Retention data",
        ],
        "produces": [
            "Causal attribution models",
            "Lifetime-value predictions",
            "Autonomous bid strategies",
            "Activation threshold analysis",
            "Budget reallocation intelligence",
            "Churn forecasting",
            "Customer intent maps",
        ],
        "cta_headline": "See Signal optimize your acquisition live.",
        "cta_subject": "MIZOKI3%20Signal%20Briefing",
        "closing_solid": True,
    },
    "capital": {
        "slug": "capital",
        "title": "Capital",
        "label": "FINANCIAL INTELLIGENCE",
        "tag": "Financial Intelligence",
        "meta_description": "Covenants tracked. Liquidity modeled. Capital governed — financial intelligence from MIZOKI3.",
        "hero_image": "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=1920&q=80&auto=format&fit=crop",
        "hero_aria": "Financial district skyline at dusk with city lights",
        "headline": "Covenants tracked. Liquidity modeled. Capital governed.",
        "hero_body": (
            "Capital gives financial leadership autonomous intelligence grounded in causal evidence — "
            "forecasting covenant breaches before they happen, stress-testing liquidity under alternate "
            "scenarios, and optimizing allocation through the same governed pipeline that enforces every "
            "other enterprise decision."
        ),
        "capabilities_label": "CAPABILITIES",
        "capabilities_headline": "From spreadsheet snapshots to causal foresight.",
        "capabilities_intro": (
            "Capital does not refresh dashboards on a schedule. It reads covenants, treasury position, and "
            "counterparty behavior as living causal nodes — projecting breach probability and liquidity "
            "stress before they become crises."
        ),
        "capabilities": [
            {
                "title": "Covenant Breach Forecasting",
                "body": (
                    "Capital monitors every financial covenant across your credit agreements, tracking the "
                    "causal factors that drive compliance metrics. When conditions shift — revenue trends, "
                    "cash flow patterns, market movements — Capital projects the breach probability and "
                    "timeline before it becomes a crisis."
                ),
            },
            {
                "title": "Liquidity Stress Modeling",
                "body": (
                    "Counterfactual simulation applied to treasury management. Capital models what happens to "
                    "your cash position under alternative scenarios — a client defaulting, a revenue line "
                    "declining, a credit facility tightening — and surfaces the causal chain behind each outcome."
                ),
            },
            {
                "title": "Capital Allocation Optimization",
                "body": (
                    "Every allocation recommendation flows through the Decision Control Plane. Capital doesn't "
                    "just suggest where to deploy resources — it justifies the recommendation with causal evidence, "
                    "simulates the alternatives, and verifies compliance with every covenant and policy constraint "
                    "before authorization."
                ),
            },
        ],
        "cross_label": "CROSS-DOMAIN INTELLIGENCE",
        "cross_headline": "Financial decisions informed by legal obligations and market signals.",
        "cross_body": (
            "When Counsel maps a new covenant restriction, Capital inherits it as a hard constraint instantly — "
            "no manual handoff, no email chain, no spreadsheet update. When Signal detects a shift in customer "
            "acquisition costs, Capital factors it into cash flow projections automatically. The knowledge graph "
            "makes financial intelligence continuous, not periodic."
        ),
        "cross_image": "https://images.unsplash.com/photo-1514565132-0f8fd0a48f18?w=1920&q=80&auto=format&fit=crop",
        "cross_aria": "Bridge at night suggesting structural connection",
        "ingests": [
            "Credit agreements & covenants",
            "Treasury data",
            "Cash flow statements",
            "Capital stack composition",
            "Market data feeds",
            "Portfolio positions",
            "Banking communications",
            "Financial projections",
        ],
        "produces": [
            "Covenant breach forecasts",
            "Liquidity stress scenarios",
            "Capital allocation recommendations",
            "Refinancing intelligence",
            "Cash flow projections",
            "Counterparty risk assessments",
            "Working capital optimization",
        ],
        "cta_headline": "See Capital model your liquidity scenarios live.",
        "cta_subject": "MIZOKI3%20Capital%20Briefing",
    },
    "risk": {
        "slug": "risk",
        "title": "Risk",
        "label": "COMPLIANCE & RESILIENCE",
        "tag": "Compliance & Resilience",
        "meta_description": "Verified continuously. Not audited annually — compliance and resilience intelligence from MIZOKI3.",
        "hero_image": "https://images.unsplash.com/photo-1541888946425-d81bb19240f5?w=1920&q=80&auto=format&fit=crop",
        "hero_aria": "Large-scale dam and reservoir suggesting containment and control",
        "headline": "Verified continuously. Not audited annually.",
        "hero_body": (
            "Risk transforms compliance from a periodic checklist into a continuous, autonomous process — "
            "monitoring regulatory changes, verifying operational alignment, and stress-testing resilience "
            "through the same causal graph that governs every enterprise decision."
        ),
        "capabilities_label": "CAPABILITIES",
        "capabilities_headline": "From periodic audits to continuous governance.",
        "capabilities_intro": (
            "Risk is not a reporting layer bolted onto other lenses. It verifies every consequential proposal "
            "in real time — arbitrating contradictions, enforcing policy, and stress-testing resilience before "
            "action reaches your systems."
        ),
        "capabilities": [
            {
                "title": "Continuous Compliance Monitoring",
                "body": (
                    "Regulatory landscapes shift constantly. Risk tracks changes across jurisdictions and "
                    "regulatory bodies, maps them to your existing obligations through the knowledge graph, "
                    "and flags gaps or conflicts before they become violations."
                ),
            },
            {
                "title": "Operational Resilience Testing",
                "body": (
                    "Risk uses counterfactual simulation to test your enterprise against failure scenarios — "
                    "a vendor defaulting, a system going offline, a regulatory change invalidating a process. "
                    "Each scenario is modeled through the causal graph, producing actionable intelligence rather "
                    "than theoretical risk scores."
                ),
            },
            {
                "title": "Cross-Domain Verification",
                "body": (
                    "Every decision authorized by the DCP is verified by Risk in real time. Legal actions "
                    "proposed by Counsel, financial movements proposed by Capital, marketing executions proposed "
                    "by Signal — all pass through Risk verification before reaching your systems."
                ),
            },
        ],
        "cross_label": "CROSS-DOMAIN INTELLIGENCE",
        "cross_headline": "Risk doesn't audit after the fact. It governs in real time.",
        "cross_body": (
            "When Capital proposes a distribution, Risk arbitrates it against Counsel-mapped covenants and "
            "simulation output before execution. When Signal reallocates budget, Risk verifies spend-governance "
            "policy. Compliance is not a quarterly report — it is the continuous conscience of the system."
        ),
        "cross_image": "https://images.unsplash.com/photo-1494412519320-aa9dfdfcb74d?w=1920&q=80&auto=format&fit=crop",
        "cross_aria": "Aerial view of a port with coordinated logistics operations",
        "ingests": [
            "Regulatory filings & updates",
            "Compliance frameworks",
            "Audit records",
            "Incident reports",
            "Operational telemetry",
            "Vendor risk data",
            "Policy documents",
            "Insurance documentation",
        ],
        "produces": [
            "Compliance gap analysis",
            "Regulatory change impact maps",
            "Resilience stress scores",
            "Vendor risk assessments",
            "Policy violation alerts",
            "Audit trail verification",
            "Operational risk forecasts",
        ],
        "cta_headline": "See Risk verify your compliance posture live.",
        "cta_subject": "MIZOKI3%20Risk%20Briefing",
    },
    "estate": {
        "slug": "estate",
        "title": "Estate",
        "label": "TRUST & ASSET INTELLIGENCE",
        "tag": "Trust & Asset Intelligence",
        "meta_description": "Structures preserved. Transfers optimized. Legacy governed — estate intelligence from MIZOKI3.",
        "hero_image": "https://images.unsplash.com/photo-1564013794819-155d6c4e8f62?w=1920&q=80&auto=format&fit=crop",
        "hero_aria": "Coastal estate property suggesting legacy and permanence",
        "headline": "Structures preserved. Transfers optimized. Legacy governed.",
        "hero_body": (
            "Estate applies autonomous decision intelligence to the most consequential financial structures — "
            "trusts, estates, multi-generational asset strategies, and tax optimization — with the same causal "
            "reasoning and governance that governs every other enterprise decision."
        ),
        "capabilities_label": "CAPABILITIES",
        "capabilities_headline": "From static estate plans to living structural intelligence.",
        "capabilities_intro": (
            "Estate does not archive documents for annual review. It models trusts, beneficiaries, and transfer "
            "pathways as a living substrate — recalculating implications when tax law, family circumstances, or "
            "market conditions change."
        ),
        "capabilities": [
            {
                "title": "Trust Structure Analysis",
                "body": (
                    "Estate maps the full topology of trust arrangements — beneficiaries, trustees, distribution "
                    "schedules, conditions, and constraints — into the knowledge graph. Every structural "
                    "relationship is tracked causally, so changes in tax law or family circumstances automatically "
                    "surface their downstream implications."
                ),
            },
            {
                "title": "Tax Strategy Optimization",
                "body": (
                    "Counterfactual simulation applied to tax planning. Estate models alternate structuring "
                    "strategies and projects their outcomes across jurisdictions, time horizons, and regulatory "
                    "scenarios — producing recommendations grounded in causal evidence rather than static assumptions."
                ),
            },
            {
                "title": "Multi-Generational Asset Intelligence",
                "body": (
                    "Estate tracks asset positions, transfer strategies, and succession plans across generational "
                    "timelines. When conditions change — a tax law update, a beneficiary event, a market shift — "
                    "the system recalculates the optimal path and surfaces it through the Decision Control Plane "
                    "for authorization."
                ),
            },
        ],
        "cross_label": "CROSS-DOMAIN INTELLIGENCE",
        "cross_headline": "Estate decisions informed by every obligation, covenant, and regulatory constraint in the system.",
        "cross_body": (
            "A covenant mapped by Counsel constrains distribution timing in Estate. A liquidity forecast from "
            "Capital bounds discretionary transfers. Risk verifies fiduciary compliance before any wire initiates. "
            "Wealth structures inherit the full enterprise context — not a siloed planning workbook."
        ),
        "cross_image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1920&q=80&auto=format&fit=crop",
        "cross_aria": "Vineyard landscape at golden hour suggesting permanence and value",
        "ingests": [
            "Trust documents & amendments",
            "Estate plans",
            "Tax filings & projections",
            "Asset registries",
            "Beneficiary records",
            "Insurance policies",
            "Property valuations",
            "Succession plans",
        ],
        "produces": [
            "Trust structure maps",
            "Tax optimization scenarios",
            "Transfer strategy recommendations",
            "Beneficiary impact analysis",
            "Generational wealth projections",
            "Regulatory compliance verification",
            "Asset rebalancing intelligence",
        ],
        "cta_headline": "See Estate model your trust structures live.",
        "cta_subject": "MIZOKI3%20Estate%20Briefing",
    },
}

ARCHITECTURE_PAGE = {
    "meta_description": (
        "Technical architecture of the MIZOKI3 autonomous decision intelligence platform — "
        "TCO-KG, SRPVDAL, and the Decision Control Plane."
    ),
    "hero_image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1920&q=80&auto=format&fit=crop",
    "hero_aria": "Modern data center corridor with server racks and ambient lighting",
    "tckg_image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80&auto=format&fit=crop",
    "tckg_aria": "Earth from space suggesting global interconnected data",
    "dcp_image": "https://images.unsplash.com/photo-1470071458764-e3fb3822ae43?w=1920&q=80&auto=format&fit=crop",
    "dcp_aria": "Horizon at dawn suggesting governance and clarity",
    "closing_image": "https://images.unsplash.com/photo-1470071458764-e3fb3822ae43?w=1920&q=80&auto=format&fit=crop",
    "closing_aria": "Expansive horizon at dawn",
}

SRPVDAL_STAGES = [
    {
        "num": "01",
        "name": "Sense",
        "description": "Ingest and contextualize signals from every domain source — contracts, treasury, media, compliance, and trust instruments.",
    },
    {
        "num": "02",
        "name": "Reason",
        "description": "Traverse causal relationships in the knowledge graph to understand what drives outcomes and what would change if conditions shifted.",
    },
    {
        "num": "03",
        "name": "Plan",
        "description": "Generate constrained candidate actions — each bound by obligations, policies, and simulated alternatives before validation.",
    },
    {
        "num": "04",
        "name": "Validate",
        "description": "Stress-test proposals against policy libraries, counterfactual simulations, and cross-lens contradictions.",
    },
    {
        "num": "05",
        "name": "Decide",
        "description": "Select, defer, or escalate through the Decision Control Plane — authorization is explicit, scored, and auditable.",
    },
    {
        "num": "06",
        "name": "Act",
        "description": "Execute only authorized payloads into enterprise systems — nothing reaches production without passing the Gate.",
    },
    {
        "num": "07",
        "name": "Learn",
        "description": "Update the graph from outcomes — every action compounds institutional memory for the next decision cycle.",
    },
]

DCP_DIMENSIONS = [
    {
        "title": "Causal Confidence",
        "description": "Strength of the causal chain supporting the proposed action — weak inference cannot authorize.",
    },
    {
        "title": "Validation Agreement",
        "description": "Alignment across independent validation agents and cross-lens verification before authorization.",
    },
    {
        "title": "Simulation Delta",
        "description": "Outcome spread between the proposed action and counterfactual alternatives modeled on the graph.",
    },
    {
        "title": "Policy Compliance",
        "description": "Conformance to regulatory frameworks, internal policy libraries, and Counsel-mapped obligations.",
    },
    {
        "title": "Historical Performance",
        "description": "Track record of similar decisions under comparable conditions — institutional memory informs the score.",
    },
]

BLOG_POSTS = [
    {
        "slug": "relu-lens-meta-algorithm",
        "href": "/blog/relu-lens-meta-algorithm.html",
        "title": "Unlocking Meta's Ad Algorithm With the ReLU Lens",
        "tag": "Marketing Intelligence",
        "subtitle": "A practical playbook for threshold-aware media buying — signal density, learning stability, and governed decision intelligence.",
        "date": "January 2026",
        "read_time": "12 min read",
        "meta_description": (
            "A practical, image-driven playbook for threshold-aware media buying: why campaigns feel dead "
            "until they activate, how to build signal density, and how MIZOKI3 operationalizes those dynamics."
        ),
        "excerpt": (
            "The canonical playbook for Meta advertisers: where signal density, learning stability, "
            "and governed decision intelligence intersect above the activation line."
        ),
    },
    {
        "slug": "decision-control-plane",
        "href": "/blog/decision-control-plane.html",
        "title": "Why Agents Need a Decision Control Plane",
        "tag": "Architecture",
        "subtitle": "The architectural innovation that separates action proposal from authorization — and why it is essential for enterprise AI.",
        "date": "March 2026",
        "read_time": "8 min read",
        "meta_description": (
            "The architectural innovation that separates action proposal from authorization — "
            "and why it is essential for enterprise AI."
        ),
        "excerpt": (
            "Why autonomous systems need explicit arbitration between action proposal, validation, "
            "and authorization — and why agents cannot bypass the Gate."
        ),
    },
    {
        "slug": "adc-decision-framework",
        "href": "/blog/adc-decision-framework.html",
        "title": "How an Autonomous Decision Controller Thinks",
        "tag": "Decision Intelligence",
        "subtitle": "A plain-English guide to the seven stages that power disciplined autonomous execution.",
        "date": "March 2026",
        "read_time": "10 min read",
        "meta_description": (
            "A plain-English guide to the seven-stage reasoning loop behind disciplined autonomous "
            "execution — from sensing a signal to measuring an outcome."
        ),
        "excerpt": (
            "A plain-English walkthrough of the seven-stage reasoning loop behind disciplined "
            "autonomous execution — from signal to governed action."
        ),
    },
]
