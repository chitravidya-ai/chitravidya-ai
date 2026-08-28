import os
from pathlib import Path

ROOT = Path("chitravidya-ai")

FILES = {}

# ---------------------------------------------------------------------------
# app.py
# ---------------------------------------------------------------------------
FILES["app.py"] = '''"""
app.py -- Chitravidya AI

Entry point for the Streamlit app. Wires together the sidebar, page
router, and global styling. Run locally with:

    streamlit run app.py

See README.md for full setup and deployment instructions.
"""

import streamlit as st

from utils.helpers import init_session_state
from components.sidebar import render_sidebar
from components.dashboard import (
    render_home_page,
    render_chapters_page,
    render_practice_page,
    render_saved_page,
    render_settings_page,
)
from components.chat import render_chat_page
from components.simulation import render_simulations_page

st.set_page_config(
    page_title="Chitravidya AI | CBSE Class 12 PCM",
    page_icon="\\U0001F393",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session_state()

LIGHT_CSS = """
<style>
    .stApp { background-color: #F7F8FC; }
    section[data-testid="stSidebar"] { background-color: #FFFFFF; border-right: 1px solid #ECEDF3; }
    div[data-testid="stChatMessage"] { background-color: #FFFFFF; border-radius: 14px; border: 1px solid #ECEDF3; }
    .stButton>button { border-radius: 10px; }
</style>
"""

DARK_CSS = """
<style>
    .stApp { background-color: #0E1117; color: #E6E6E6; }
    section[data-testid="stSidebar"] { background-color: #12141B; border-right: 1px solid #22242E; }
    div[data-testid="stChatMessage"] { background-color: #1A1D27; border-radius: 14px; border: 1px solid #22242E; }
    .stButton>button { border-radius: 10px; }
</style>
"""

st.markdown(DARK_CSS if st.session_state.theme == "dark" else LIGHT_CSS, unsafe_allow_html=True)

render_sidebar()

PAGE_RENDERERS = {
    "Home": render_home_page,
    "AI Tutor": render_chat_page,
    "Physics Simulations": render_simulations_page,
    "PCM Chapters": render_chapters_page,
    "Practice": render_practice_page,
    "Saved": render_saved_page,
    "Settings": render_settings_page,
}

try:
    renderer = PAGE_RENDERERS.get(st.session_state.current_page, render_home_page)
    renderer()
except Exception:
    st.error(
        "\\u26A0\\uFE0F Something unexpected went wrong loading this page. "
        "Please try refreshing, or use the sidebar to go back to Home."
    )
'''

# ---------------------------------------------------------------------------
# requirements.txt
# ---------------------------------------------------------------------------
FILES["requirements.txt"] = """streamlit>=1.38.0
anthropic>=0.40.0
"""

# ---------------------------------------------------------------------------
# .gitignore
# ---------------------------------------------------------------------------
FILES[".gitignore"] = """# Secrets -- never commit real API keys
.streamlit/secrets.toml

# Python
__pycache__/
*.pyc
*.pyo
.venv/
venv/
env/
*.egg-info/

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/

# Streamlit
.streamlit/logs/
"""

# ---------------------------------------------------------------------------
# .streamlit/config.toml
# ---------------------------------------------------------------------------
FILES[".streamlit/config.toml"] = """[theme]
primaryColor = "#5B5FEF"
backgroundColor = "#F7F8FC"
secondaryBackgroundColor = "#FFFFFF"
textColor = "#1A1C29"
font = "sans serif"

[server]
headless = true
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
"""

# ---------------------------------------------------------------------------
# .streamlit/secrets.toml.example
# ---------------------------------------------------------------------------
FILES[".streamlit/secrets.toml.example"] = """# Copy this file to .streamlit/secrets.toml (local dev) and NEVER commit the
# real secrets.toml to GitHub. On Streamlit Community Cloud, paste the same
# key/value into your app's "Secrets" settings panel instead of using a file.

ANTHROPIC_API_KEY = "sk-ant-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
"""

# ---------------------------------------------------------------------------
# data/physics.py
# ---------------------------------------------------------------------------
FILES["data/physics.py"] = '''"""
CBSE Class 12 Physics syllabus data (2026-27 session).

This structure mirrors the CBSE curriculum (verified against the CBSE
2025-26 circular; CBSE has historically carried this structure forward
unchanged, but you should cross-check against the official 2026-27
circular at cbseacademic.nic.in before publishing to students, and update
this file if CBSE issues any revision).

Each chapter entry also lists a small set of "keywords" used purely as a
lightweight, best-effort UI hint for subject/topic tagging. The actual
understanding of a student's question is done by the AI model itself via
the system prompt in services/ai_service.py -- this file is NOT used to
restrict or hard-code what the AI can answer, only to power the syllabus
browser UI and give the AI a grounded reference list so it never invents
chapters that aren't on the syllabus.
"""

PHYSICS_SYLLABUS = {
    "subject": "Physics",
    "emoji": "\\u26A1",
    "class_level": "CBSE Class 12",
    "session": "2026-27",
    "total_theory_marks": 70,
    "total_practical_marks": 30,
    "units": [
        {
            "unit_no": 1,
            "unit_name": "Electrostatics",
            "marks": 16,
            "chapters": [
                {
                    "chapter_no": 1,
                    "title": "Electric Charges and Fields",
                    "keywords": ["charge", "coulomb's law", "electric field", "gauss's law",
                                 "dipole", "flux", "field lines"],
                },
                {
                    "chapter_no": 2,
                    "title": "Electrostatic Potential and Capacitance",
                    "keywords": ["potential", "capacitor", "capacitance", "dielectric",
                                 "equipotential", "energy stored in capacitor"],
                },
            ],
        },
        {
            "unit_no": 2,
            "unit_name": "Current Electricity",
            "marks": 17,
            "chapters": [
                {
                    "chapter_no": 3,
                    "title": "Current Electricity",
                    "keywords": ["ohm's law", "resistivity", "emf", "internal resistance",
                                 "wheatstone bridge", "potentiometer", "kirchhoff's laws",
                                 "drift velocity"],
                },
            ],
        },
        {
            "unit_no": 3,
            "unit_name": "Magnetic Effects of Current and Magnetism",
            "marks": 17,
            "chapters": [
                {
                    "chapter_no": 4,
                    "title": "Moving Charges and Magnetism",
                    "keywords": ["biot-savart law", "ampere's law", "solenoid", "cyclotron",
                                 "force on a moving charge", "magnetic field due to current"],
                },
                {
                    "chapter_no": 5,
                    "title": "Magnetism and Matter",
                    "keywords": ["bar magnet", "earth's magnetism", "magnetic dipole",
                                 "diamagnetic", "paramagnetic", "ferromagnetic"],
                },
            ],
        },
        {
            "unit_no": 4,
            "unit_name": "Electromagnetic Induction and Alternating Currents",
            "marks": 18,
            "chapters": [
                {
                    "chapter_no": 6,
                    "title": "Electromagnetic Induction",
                    "keywords": ["faraday's law", "lenz's law", "induced emf", "eddy currents",
                                 "self inductance", "mutual inductance"],
                },
                {
                    "chapter_no": 7,
                    "title": "Alternating Current",
                    "keywords": ["ac circuit", "lc oscillation", "resonance", "transformer",
                                 "rms value", "impedance", "power factor"],
                },
            ],
        },
        {
            "unit_no": 5,
            "unit_name": "Electromagnetic Waves",
            "marks": 18,
            "chapters": [
                {
                    "chapter_no": 8,
                    "title": "Electromagnetic Waves",
                    "keywords": ["displacement current", "em spectrum", "properties of em waves"],
                },
                {
                    "chapter_no": 9,
                    "title": "Ray Optics and Optical Instruments",
                    "keywords": ["reflection", "refraction", "lens formula", "mirror formula",
                                 "total internal reflection", "prism", "microscope", "telescope"],
                },
                {
                    "chapter_no": 10,
                    "title": "Wave Optics",
                    "keywords": ["huygens principle", "interference", "young's double slit",
                                 "diffraction", "polarisation"],
                },
            ],
        },
        {
            "unit_no": 6,
            "unit_name": "Dual Nature of Radiation and Matter",
            "marks": 12,
            "chapters": [
                {
                    "chapter_no": 11,
                    "title": "Dual Nature of Radiation and Matter",
                    "keywords": ["photoelectric effect", "einstein's equation", "de broglie wavelength",
                                 "work function", "matter waves"],
                },
            ],
        },
        {
            "unit_no": 7,
            "unit_name": "Atoms and Nuclei",
            "marks": 12,
            "chapters": [
                {
                    "chapter_no": 12,
                    "title": "Atoms",
                    "keywords": ["bohr model", "rutherford model", "hydrogen spectrum"],
                },
                {
                    "chapter_no": 13,
                    "title": "Nuclei",
                    "keywords": ["radioactivity", "binding energy", "nuclear fission",
                                 "nuclear fusion", "mass defect", "half life"],
                },
            ],
        },
        {
            "unit_no": 8,
            "unit_name": "Electronic Devices",
            "marks": 7,
            "chapters": [
                {
                    "chapter_no": 14,
                    "title": "Semiconductor Electronics: Materials, Devices and Simple Circuits",
                    "keywords": ["pn junction diode", "zener diode", "transistor", "rectifier",
                                 "semiconductor", "logic gates"],
                },
            ],
        },
    ],
}


def all_chapter_titles():
    """Flat list of every Class 12 Physics chapter title, in syllabus order."""
    titles = []
    for unit in PHYSICS_SYLLABUS["units"]:
        for ch in unit["chapters"]:
            titles.append(ch["title"])
    return titles


def flat_chapters():
    """Flat list of chapter dicts, each tagged with its parent unit name/marks."""
    flat = []
    for unit in PHYSICS_SYLLABUS["units"]:
        for ch in unit["chapters"]:
            entry = dict(ch)
            entry["unit_name"] = unit["unit_name"]
            entry["unit_marks"] = unit["marks"]
            flat.append(entry)
    return flat
'''

# ---------------------------------------------------------------------------
# data/chemistry.py
# ---------------------------------------------------------------------------
FILES["data/chemistry.py"] = '''"""
CBSE Class 12 Chemistry syllabus data (2026-27 session).

See the note at the top of data/physics.py -- same caveats apply: this
mirrors the CBSE 2025-26 circular structure and should be cross-checked
against the official 2026-27 circular before publishing.
"""

CHEMISTRY_SYLLABUS = {
    "subject": "Chemistry",
    "emoji": "\\U0001F9EA",
    "class_level": "CBSE Class 12",
    "session": "2026-27",
    "total_theory_marks": 70,
    "total_practical_marks": 30,
    "units": [
        {
            "unit_no": 1,
            "unit_name": "Solutions",
            "marks": 7,
            "chapters": [
                {
                    "chapter_no": 1,
                    "title": "Solutions",
                    "keywords": ["molarity", "molality", "raoult's law", "colligative properties",
                                 "van't hoff factor", "osmotic pressure"],
                },
            ],
        },
        {
            "unit_no": 2,
            "unit_name": "Electrochemistry",
            "marks": 9,
            "chapters": [
                {
                    "chapter_no": 2,
                    "title": "Electrochemistry",
                    "keywords": ["nernst equation", "galvanic cell", "electrolysis", "emf of cell",
                                 "conductivity", "kohlrausch's law", "fuel cell"],
                },
            ],
        },
        {
            "unit_no": 3,
            "unit_name": "Chemical Kinetics",
            "marks": 7,
            "chapters": [
                {
                    "chapter_no": 3,
                    "title": "Chemical Kinetics",
                    "keywords": ["rate of reaction", "order of reaction", "rate law",
                                 "arrhenius equation", "activation energy", "half life"],
                },
            ],
        },
        {
            "unit_no": 4,
            "unit_name": "d- and f-Block Elements",
            "marks": 7,
            "chapters": [
                {
                    "chapter_no": 4,
                    "title": "d- and f-Block Elements",
                    "keywords": ["transition elements", "lanthanoids", "actinoids",
                                 "variable oxidation states", "colour of transition metal ions"],
                },
            ],
        },
        {
            "unit_no": 5,
            "unit_name": "Coordination Compounds",
            "marks": 7,
            "chapters": [
                {
                    "chapter_no": 5,
                    "title": "Coordination Compounds",
                    "keywords": ["werner's theory", "ligand", "coordination number", "IUPAC naming",
                                 "crystal field theory", "isomerism in coordination compounds"],
                },
            ],
        },
        {
            "unit_no": 6,
            "unit_name": "Haloalkanes and Haloarenes",
            "marks": 6,
            "chapters": [
                {
                    "chapter_no": 6,
                    "title": "Haloalkanes and Haloarenes",
                    "keywords": ["sn1", "sn2", "nucleophilic substitution", "grignard reagent",
                                 "optical isomerism"],
                },
            ],
        },
        {
            "unit_no": 7,
            "unit_name": "Alcohols, Phenols and Ethers",
            "marks": 6,
            "chapters": [
                {
                    "chapter_no": 7,
                    "title": "Alcohols, Phenols and Ethers",
                    "keywords": ["lucas test", "williamson synthesis", "acidity of phenol",
                                 "dehydration of alcohol"],
                },
            ],
        },
        {
            "unit_no": 8,
            "unit_name": "Aldehydes, Ketones and Carboxylic Acids",
            "marks": 8,
            "chapters": [
                {
                    "chapter_no": 8,
                    "title": "Aldehydes, Ketones and Carboxylic Acids",
                    "keywords": ["nucleophilic addition", "aldol condensation", "cannizzaro reaction",
                                 "haloform reaction", "acidity of carboxylic acid"],
                },
            ],
        },
        {
            "unit_no": 9,
            "unit_name": "Amines",
            "marks": 6,
            "chapters": [
                {
                    "chapter_no": 9,
                    "title": "Amines",
                    "keywords": ["basicity of amines", "hofmann bromamide reaction",
                                 "diazonium salts", "gabriel phthalimide synthesis"],
                },
            ],
        },
        {
            "unit_no": 10,
            "unit_name": "Biomolecules",
            "marks": 7,
            "chapters": [
                {
                    "chapter_no": 10,
                    "title": "Biomolecules",
                    "keywords": ["carbohydrates", "proteins", "enzymes", "vitamins",
                                 "nucleic acids", "hormones"],
                },
            ],
        },
    ],
}


def all_chapter_titles():
    titles = []
    for unit in CHEMISTRY_SYLLABUS["units"]:
        for ch in unit["chapters"]:
            titles.append(ch["title"])
    return titles


def flat_chapters():
    flat = []
    for unit in CHEMISTRY_SYLLABUS["units"]:
        for ch in unit["chapters"]:
            entry = dict(ch)
            entry["unit_name"] = unit["unit_name"]
            entry["unit_marks"] = unit["marks"]
            flat.append(entry)
    return flat
'''

# ---------------------------------------------------------------------------
# data/mathematics.py
# ---------------------------------------------------------------------------
FILES["data/mathematics.py"] = '''"""
CBSE Class 12 Mathematics syllabus data (2026-27 session).

See the note at the top of data/physics.py -- same caveats apply: this
mirrors the CBSE 2025-26 circular structure and should be cross-checked
against the official 2026-27 circular before publishing.
"""

MATHEMATICS_SYLLABUS = {
    "subject": "Mathematics",
    "emoji": "\\U0001F4D0",
    "class_level": "CBSE Class 12",
    "session": "2026-27",
    "total_theory_marks": 80,
    "total_internal_assessment_marks": 20,
    "units": [
        {
            "unit_no": 1,
            "unit_name": "Relations and Functions",
            "chapters": [
                {
                    "chapter_no": 1,
                    "title": "Relations and Functions",
                    "keywords": ["reflexive", "symmetric", "transitive", "equivalence relation",
                                 "one-one function", "onto function", "bijective"],
                },
                {
                    "chapter_no": 2,
                    "title": "Inverse Trigonometric Functions",
                    "keywords": ["principal value", "arcsin", "arccos", "arctan",
                                 "domain and range of inverse trig functions"],
                },
            ],
        },
        {
            "unit_no": 2,
            "unit_name": "Algebra",
            "chapters": [
                {
                    "chapter_no": 3,
                    "title": "Matrices",
                    "keywords": ["matrix operations", "transpose", "symmetric matrix",
                                 "invertible matrix", "elementary row operations"],
                },
                {
                    "chapter_no": 4,
                    "title": "Determinants",
                    "keywords": ["cofactor", "adjoint", "inverse of a matrix", "cramer's rule",
                                 "area of triangle using determinants"],
                },
            ],
        },
        {
            "unit_no": 3,
            "unit_name": "Calculus",
            "chapters": [
                {
                    "chapter_no": 5,
                    "title": "Continuity and Differentiability",
                    "keywords": ["continuity", "differentiability", "chain rule",
                                 "logarithmic differentiation", "second order derivative",
                                 "mean value theorem"],
                },
                {
                    "chapter_no": 6,
                    "title": "Application of Derivatives",
                    "keywords": ["increasing decreasing function", "maxima minima",
                                 "rate of change", "tangent and normal", "approximation"],
                },
                {
                    "chapter_no": 7,
                    "title": "Integrals",
                    "keywords": ["indefinite integral", "definite integral", "integration by parts",
                                 "integration by substitution", "partial fractions"],
                },
                {
                    "chapter_no": 8,
                    "title": "Application of the Integrals",
                    "keywords": ["area under curve", "area between two curves"],
                },
                {
                    "chapter_no": 9,
                    "title": "Differential Equations",
                    "keywords": ["order and degree", "variable separable", "homogeneous differential equation",
                                 "linear differential equation", "integrating factor"],
                },
            ],
        },
        {
            "unit_no": 4,
            "unit_name": "Vectors and Three-Dimensional Geometry",
            "chapters": [
                {
                    "chapter_no": 10,
                    "title": "Vectors",
                    "keywords": ["dot product", "cross product", "scalar triple product",
                                 "direction cosines", "unit vector"],
                },
                {
                    "chapter_no": 11,
                    "title": "Three-dimensional Geometry",
                    "keywords": ["equation of a line in 3d", "equation of a plane",
                                 "angle between two lines", "shortest distance between lines"],
                },
            ],
        },
        {
            "unit_no": 5,
            "unit_name": "Linear Programming",
            "chapters": [
                {
                    "chapter_no": 12,
                    "title": "Linear Programming",
                    "keywords": ["feasible region", "objective function", "corner point method",
                                 "optimal solution"],
                },
            ],
        },
        {
            "unit_no": 6,
            "unit_name": "Probability",
            "chapters": [
                {
                    "chapter_no": 13,
                    "title": "Probability",
                    "keywords": ["conditional probability", "bayes' theorem", "random variable",
                                 "probability distribution", "bernoulli trials", "binomial distribution"],
                },
            ],
        },
    ],
}


def all_chapter_titles():
    titles = []
    for unit in MATHEMATICS_SYLLABUS["units"]:
        for ch in unit["chapters"]:
            titles.append(ch["title"])
    return titles


def flat_chapters():
    flat = []
    for unit in MATHEMATICS_SYLLABUS["units"]:
        for ch in unit["chapters"]:
            entry = dict(ch)
            entry["unit_name"] = unit["unit_name"]
            flat.append(entry)
    return flat
'''

# ---------------------------------------------------------------------------
# services/syllabus_service.py
# ---------------------------------------------------------------------------
FILES["services/syllabus_service.py"] = '''"""
services/syllabus_service.py

A thin, unified access layer over data/physics.py, data/chemistry.py and
data/mathematics.py. Nothing here calls any AI model -- this module only
organizes syllabus-ground-truth data so:

1. The "PCM Chapters" page in the UI can render it.
2. ai_service.py can inject a compact, accurate chapter list into the
   system prompt so the model always has real CBSE Class 12 PCM chapter
   names to ground its answers in (and knows what is genuinely outside
   the syllabus).
3. A lightweight keyword-based subject guess can be made for the UI's
   subject indicator badge, *before* the AI call returns (the AI's own
   understanding of the question is the real subject-detection layer --
   this is just a fast, best-effort visual hint).
"""

from data.physics import PHYSICS_SYLLABUS, flat_chapters as _physics_flat
from data.chemistry import CHEMISTRY_SYLLABUS, flat_chapters as _chemistry_flat
from data.mathematics import MATHEMATICS_SYLLABUS, flat_chapters as _maths_flat

SUBJECTS = {
    "Physics": PHYSICS_SYLLABUS,
    "Chemistry": CHEMISTRY_SYLLABUS,
    "Mathematics": MATHEMATICS_SYLLABUS,
}

SUBJECT_EMOJI = {
    "Physics": "\\u26A1",
    "Chemistry": "\\U0001F9EA",
    "Mathematics": "\\U0001F4D0",
}


def get_syllabus(subject: str):
    """Return the raw syllabus dict for a subject name ('Physics' etc.)."""
    return SUBJECTS.get(subject)


def get_all_flat_chapters():
    """Return {subject_name: [chapter_dict, ...]} for all three subjects."""
    return {
        "Physics": _physics_flat(),
        "Chemistry": _chemistry_flat(),
        "Mathematics": _maths_flat(),
    }


def build_syllabus_reference_text():
    """
    Build a compact plain-text chapter reference (subject -> unit -> chapters)
    for injection into the AI system prompt, so the model is grounded in the
    real CBSE Class 12 PCM chapter list rather than guessing from memory.
    """
    lines = []
    for subject_name, syllabus in SUBJECTS.items():
        lines.append(f"\\n{syllabus['emoji']} {subject_name} ({syllabus['class_level']}, {syllabus['session']}):")
        for unit in syllabus["units"]:
            chapter_titles = ", ".join(ch["title"] for ch in unit["chapters"])
            lines.append(f"  - Unit {unit['unit_no']} - {unit['unit_name']}: {chapter_titles}")
    return "\\n".join(lines)


_KEYWORD_INDEX = None


def _build_keyword_index():
    """Build a {keyword: subject_name} lookup once, lazily, from all chapter keywords."""
    global _KEYWORD_INDEX
    if _KEYWORD_INDEX is not None:
        return _KEYWORD_INDEX

    index = {}
    for subject_name, flat_fn in (
        ("Physics", _physics_flat),
        ("Chemistry", _chemistry_flat),
        ("Mathematics", _maths_flat),
    ):
        for ch in flat_fn():
            for kw in ch.get("keywords", []):
                index[kw.lower()] = subject_name
            index[ch["title"].lower()] = subject_name
    _KEYWORD_INDEX = index
    return index


def guess_subject(question: str):
    """
    Best-effort, fast keyword match used ONLY to pre-populate a UI badge
    before the AI's real response arrives. Returns a subject name or None.
    This is a hint, not the source of truth -- the AI response itself may
    correct/override it and the UI should prefer whatever the AI actually
    answered about.
    """
    if not question:
        return None
    q = question.lower()
    index = _build_keyword_index()

    for kw in sorted(index.keys(), key=len, reverse=True):
        if kw in q:
            return index[kw]

    physics_hints = ["physics", "numerical", "circuit", "wave", "force", "voltage", "current"]
    chemistry_hints = ["chemistry", "reaction", "compound", "acid", "bond", "organic", "equation balance"]
    maths_hints = ["maths", "math", "integrate", "differentiate", "derivative", "matrix", "probability", "vector"]

    for hint in physics_hints:
        if hint in q:
            return "Physics"
    for hint in chemistry_hints:
        if hint in q:
            return "Chemistry"
    for hint in maths_hints:
        if hint in q:
            return "Mathematics"

    return None
'''

# ---------------------------------------------------------------------------
# services/simulation_service.py
# ---------------------------------------------------------------------------
FILES["services/simulation_service.py"] = '''"""
services/simulation_service.py

A small, hand-curated map of CBSE Class 12 Physics topics to real PhET
Interactive Simulations (https://phet.colorado.edu). This is intentionally
a *whitelist*: the AI is instructed (see ai_service.py) to only ever
reference a simulation that appears in this file, and to say plainly that
no suitable simulation is available otherwise.

IMPORTANT FOR MAINTAINERS: before shipping to real students, click through
every URL below to confirm it still resolves on phet.colorado.edu -- PhET
occasionally renames or retires simulations.
"""

SIMULATIONS = {
    "Electric Charges and Fields": {
        "title": "Charges and Fields",
        "url": "https://phet.colorado.edu/en/simulations/charges-and-fields",
        "try_this": [
            "Place a positive and a negative charge on the grid.",
            "Drag an E-field sensor around and watch the field vectors change.",
            "Add more charges and see how the field lines rearrange.",
        ],
    },
    "Electrostatic Potential and Capacitance": {
        "title": "Capacitor Lab: Basics",
        "url": "https://phet.colorado.edu/en/simulations/capacitor-
