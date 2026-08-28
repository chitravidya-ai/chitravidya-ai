import streamlit as st
from openai import OpenAI
import re

# ============================================================
# CHITRAVIDYA AI
# CBSE CLASS 12 PCM LEARNING PLATFORM
# ============================================================

st.set_page_config(
    page_title="Chitravidya AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

.brand {
    font-size: 26px;
    font-weight: 800;
    padding: 8px 0 20px 0;
}

.hero {
    text-align:center;
    padding:70px 20px 30px;
}

.hero-title {
    font-size:52px;
    font-weight:800;
    letter-spacing:-2px;
}

.hero-subtitle {
    font-size:19px;
    opacity:.65;
    margin-top:12px;
}

.feature-card {
    border:1px solid rgba(128,128,128,.22);
    border-radius:20px;
    padding:25px;
    min-height:170px;
    background:rgba(128,128,128,.04);
}

.feature-card:hover {
    border-color:rgba(128,128,128,.5);
}

.sim-card {
    border:1px solid rgba(128,128,128,.25);
    border-radius:20px;
    padding:24px;
    margin-top:20px;
}

.step {
    border-left:3px solid #777;
    padding:10px 18px;
    margin:10px 0;
}

.subject-badge {
    display:inline-block;
    padding:5px 12px;
    border-radius:20px;
    border:1px solid rgba(128,128,128,.3);
    font-size:13px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SESSION
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "page" not in st.session_state:
    st.session_state.page = "Home"

# ============================================================
# OPENAI
# ============================================================

try:
    client = OpenAI(
        api_key=st.secrets["OPENAI_API_KEY"]
    )
    AI_READY = True
except Exception:
    client = None
    AI_READY = False


# ============================================================
# PHET DATABASE
# ============================================================
#
# IMPORTANT:
# Only add verified PhET URLs here.
# Do not invent URLs.
#

PHET_DATABASE = {

    "solenoid": {
        "title": "Solenoids",
        "url": "https://phet.colorado.edu/en/activities/4547",
        "subject": "Physics",
        "topic": "Moving Charges and Magnetism",
        "steps": [
            "Open the simulation.",
            "Read the controls before changing anything.",
            "Observe how the coil/solenoid behaves.",
            "Change the available variables one at a time.",
            "Observe how the magnetic effect changes.",
            "Connect what you observe with the Class 12 concept."
        ]
    },

    "electromagnet": {
        "title": "Magnets and Electromagnets",
        "url": "https://phet.colorado.edu/sims/html/magnets-and-electromagnets/latest/magnets-and-electromagnets_all.html",
        "subject": "Physics",
        "topic": "Moving Charges and Magnetism",
        "steps": [
            "Open the Electromagnet screen.",
            "Observe the magnetic field.",
            "Change the available controls.",
            "Observe how the magnetic effect changes.",
            "Relate your observation to electromagnets."
        ]
    },

    "faraday": {
        "title": "Faraday's Electromagnetic Lab",
        "url": "https://phet.colorado.edu/sims/html/faradays-electromagnetic-lab/latest/faradays-electromagnetic-lab_all.html",
        "subject": "Physics",
        "topic": "Electromagnetic Induction",
        "steps": [
            "Open the simulation.",
            "Select the Pickup Coil or Electromagnet screen.",
            "Move/change the magnetic setup.",
            "Observe the effect on the circuit.",
            "Connect the observation with electromagnetic induction."
        ]
    }
}


# ============================================================
# DETECT PHET TOPIC
# ============================================================

def find_phet_simulation(question):

    q = question.lower()

    keywords = {
        "solenoid": "solenoid",
        "solenoids": "solenoid",

        "electromagnet": "electromagnet",
        "electromagnetic": "electromagnet",

        "faraday": "faraday",
        "electromagnetic induction": "faraday",
        "induction": "faraday"
    }

    for keyword, sim_key in keywords.items():

        if keyword in q:
            return PHET_DATABASE[sim_key]

    return None


# ============================================================
# SUBJECT DETECTION
# ============================================================

def detect_subject(question):

    q = question.lower()

    physics_words = [
        "force", "electric", "magnetic", "current",
        "voltage", "charge", "field", "ray", "lens",
        "mirror", "wave", "atom", "nucleus",
        "solenoid", "capacitor", "resistance",
        "emf", "induction", "physics"
    ]

    chemistry_words = [
        "reaction", "organic", "benzene", "amine",
        "alcohol", "aldehyde", "ketone", "electrochemistry",
        "solution", "kinetics", "coordination",
        "chemistry", "oxidation", "reduction"
    ]

    maths_words = [
        "integral", "integration", "derivative",
        "differentiation", "matrix", "determinant",
        "probability", "vector", "differential",
        "trigonometry", "continuity", "matrices",
        "mathematics", "maths"
    ]

    if any(word in q for word in physics_words):
        return "Physics"

    if any(word in q for word in chemistry_words):
        return "Chemistry"

    if any(word in q for word in maths_words):
        return "Mathematics"

    return "PCM"


# ============================================================
# AI SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
You are Chitravidya AI.

You are an educational AI tutor ONLY for CBSE Class 12 PCM.

PCM:
- Physics
- Chemistry
- Mathematics

Your target curriculum is CBSE Class 12 for the 2026-27 academic
session.

Your most important objective is ACCURACY.

Understand questions written in:
- English
- Hindi
- Hinglish
- Informal student language
- Short forms
- Spelling mistakes

Never require perfect grammar.

Examples:

"bhai solenoid samjha"

"what is solenoid"

"solenoid kya hota h"

"magnetic field due to solenoid explain"

All should be understood as the same concept.

==================================================
ANSWER STYLE
==================================================

For a normal concept question:

### Simple Explanation

Give a very easy explanation.

### Key Points

Give approximately 3-4 important points.

### Formula

Give the correct formula when applicable.

### CBSE Point

Give the important Class 12 exam-oriented point.

Do NOT unnecessarily make answers huge.

==================================================
NUMERICALS
==================================================

Use:

Given:
To Find:
Formula:
Solution:
Final Answer:

Show every important mathematical step.

Check calculations carefully.

==================================================
DERIVATIONS
==================================================

Give a proper step-by-step Class 12 CBSE level derivation.

==================================================
ACCURACY
==================================================

Never invent:
- formulas
- facts
- syllabus topics
- PhET simulations
- exam guarantees

If you are unsure, clearly say so.

Do not claim a question is guaranteed to appear in CBSE.

==================================================
LANGUAGE
==================================================

English question → English answer.

Hindi question → Hindi answer.

Hinglish question → Hinglish answer.

==================================================
SCOPE
==================================================

Stay focused on Class 12 CBSE PCM.

If a question is clearly outside the core syllabus,
tell the student that it is outside the core Class 12 PCM scope.

Do not pretend it is part of CBSE Class 12.
"""


# ============================================================
# AI FUNCTION
# ============================================================

def ask_ai(question):

    if not AI_READY:

        return """
### AI setup required

The OpenAI API key is not configured.

Add `OPENAI_API_KEY` inside Streamlit Secrets.
"""

    history = ""

    for message in st.session_state.messages[-8:]:
        history += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )

    prompt = f"""
{SYSTEM_PROMPT}

Conversation history:
{history}

Current student question:
{question}

Answer the student now.
"""

    try:

        response = client.responses.create(
            model="gpt-5",
            instructions=SYSTEM_PROMPT,
            input=prompt
        )

        return response.output_text

    except Exception as error:

        return (
            "Sorry, I couldn't connect to the AI right now. "
            "Please try again."
        )


# ============================================================
# SIMULATION CARD
# ============================================================

def show_simulation(sim):

    st.markdown(
        f"""
        <div class="sim-card">

        <h2>⚡ Interactive Simulation</h2>

        <h3>{sim['title']}</h3>

        <p>
        <b>Subject:</b> {sim['subject']}<br>
        <b>Topic:</b> {sim['topic']}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "🚀 Open PhET Simulation",
        sim["url"],
        use_container_width=True
    )

    st.markdown("### 🧑‍🎓 Beginner Guide")

    for number, step in enumerate(sim["steps"], 1):

        st.markdown(
            f"""
            <div class="step">
            <b>Step {number}</b><br>
            {step}
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="brand">🧠 Chitravidya AI</div>',
        unsafe_allow_html=True
    )

    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"

    if st.button("💬 AI Tutor", use_container_width=True):
        st.session_state.page = "AI Tutor"

    if st.button("⚡ Simulations", use_container_width=True):
        st.session_state.page = "Simulations"

    if st.button("📚 PCM Chapters", use_container_width=True):
        st.session_state.page = "PCM Chapters"

    if st.button("📝 Practice", use_container_width=True):
        st.session_state.page = "Practice"

    st.divider()

    st.caption("CBSE Class 12")
    st.caption("Physics • Chemistry • Mathematics")
    st.caption("Academic Session 2026–27")


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "Home":

    st.markdown(
        """
        <div class="hero">

        <div class="hero-title">
        Learn PCM.<br>
        Understand Everything.
        </div>

        <div class="hero-subtitle">
        Your AI-powered Class 12 CBSE Physics, Chemistry
        & Mathematics learning companion.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    question = st.chat_input(
        "Ask anything from Class 12 PCM..."
    )

    if question:

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        answer = ask_ai(question)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.session_state.page = "AI Tutor"

        st.rerun()

    st.markdown("### What can you learn?")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """
            <div class="feature-card">
            <h2>⚡ Physics</h2>
            <p>
            Concepts, formulas, derivations,
            numericals and interactive simulations.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            """
            <div class="feature-card">
            <h2>🧪 Chemistry</h2>
            <p>
            Reactions, mechanisms, concepts,
            equations and numericals.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            """
            <div class="feature-card">
            <h2>📐 Mathematics</h2>
            <p>
            Step-by-step mathematical problem solving
            for Class 12 CBSE.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# AI TUTOR
# ============================================================

elif st.session_state.page == "AI Tutor":

    st.title("💬 Chitravidya AI")

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            if message["role"] == "assistant":

                sim = find_phet_simulation(
                    st.session_state.messages[
                        max(
                            0,
                            st.session_state.messages.index(message)-1
                        )
                    ]["content"]
                    if len(st.session_state.messages) > 1
                    else ""
                )

                if sim:
                    show_simulation(sim)

    question = st.chat_input(
        "Ask your PCM question..."
    )

    if question:

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):

            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                answer = ask_ai(question)

            st.markdown(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        sim = find_phet_simulation(question)

        if sim:
            show_simulation(sim)


# ============================================================
# SIMULATIONS
# ============================================================

elif st.session_state.page == "Simulations":

    st.title("⚡ Physics Simulations")

    st.write(
        "Learn Physics by interacting with simulations."
    )

    for sim in PHET_DATABASE.values():

        show_simulation(sim)


# ============================================================
# PCM
# ============================================================

elif st.session_state.page == "PCM Chapters":

    st.title("📚 Class 12 PCM")

    physics = [
        "Electric Charges and Fields",
        "Electrostatic Potential and Capacitance",
        "Current Electricity",
        "Moving Charges and Magnetism",
        "Magnetism and Matter",
        "Electromagnetic Induction",
        "Alternating Current",
        "Electromagnetic Waves",
        "Ray Optics and Optical Instruments",
        "Wave Optics",
        "Dual Nature of Radiation and Matter",
        "Atoms",
        "Nuclei",
        "Semiconductor Electronics"
    ]

    chemistry = [
        "Solutions",
        "Electrochemistry",
        "Chemical Kinetics",
        "d and f Block Elements",
        "Coordination Compounds",
        "Haloalkanes and Haloarenes",
        "Alcohols, Phenols and Ethers",
        "Aldehydes, Ketones and Carboxylic Acids",
        "Amines",
        "Biomolecules"
    ]

    mathematics = [
        "Relations and Functions",
        "Inverse Trigonometric Functions",
        "Matrices",
        "Determinants",
        "Continuity and Differentiability",
        "Applications of Derivatives",
        "Integrals",
        "Applications of Integrals",
        "Differential Equations",
        "Vector Algebra",
        "Three Dimensional Geometry",
        "Linear Programming",
        "Probability"
    ]

    tab1, tab2, tab3 = st.tabs(
        ["⚡ Physics", "🧪 Chemistry", "📐 Mathematics"]
    )

    with tab1:

        for item in physics:
            st.write("⚡", item)

    with tab2:

        for item in chemistry:
            st.write("🧪", item)

    with tab3:

        for item in mathematics:
            st.write("📐", item)


# ============================================================
# PRACTICE
# ============================================================

elif st.session_state.page == "Practice":

    st.title("📝 Practice")

    subject = st.selectbox(
        "Choose Subject",
        ["Physics", "Chemistry", "Mathematics"]
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Basic", "Moderate", "Board Level"]
    )

    if st.button(
        "Generate Question",
        use_container_width=True
    ):

        if AI_READY:

            prompt = f"""
Generate ONE {difficulty} CBSE Class 12
{subject} practice question.

Keep it within Class 12 CBSE level.

Do not provide the answer yet.
"""

            response = client.responses.create(
                model="gpt-5",
                instructions=SYSTEM_PROMPT,
                input=prompt
            )

            st.markdown("### Question")

            st.info(response.output_text)

        else:

            st.error(
                "Configure OPENAI_API_KEY first."
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Chitravidya AI • CBSE Class 12 PCM • "
    "Ask • Understand • Visualize • Practice"
)
