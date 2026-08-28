import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="ChitraVidya AI | Class 12 PCM",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS: Hide PhET logo/3-dots on right bottom & keep sound icon intact
st.markdown("""
    <style>
    .title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        margin-top: 1vh;
        margin-bottom: 0px;
    }
    .logo-img {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        object-fit: cover;
    }
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(45deg, #4F46E5, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .sub-title {
        text-align: center;
        font-size: 1.1rem;
        color: #9CA3AF;
        margin-bottom: 1.5rem;
        font-weight: 500;
    }
    /* Simulation Container with overlay to hide bottom-right PhET branding */
    .sim-container {
        position: relative;
        height: 550px;
        overflow: hidden;
        border-radius: 12px;
        border: 1px solid #374151;
        background: #0f172a;
        margin-bottom: 10px;
    }
    .sim-container iframe {
        width: 100%;
        height: 100%;
        border: none;
    }
    /* Overlay box hiding PhET Logo & 3 Dots on bottom right corner */
    .brand-overlay {
        position: absolute;
        bottom: 0;
        right: 0;
        width: 150px;
        height: 42px;
        background-color: #0d1117;
        z-index: 10;
        pointer-events: auto;
    }
    .topic-card {
        background-color: #1E293B;
        border: 1px solid #334155;
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .topic-title {
        color: #38BDF8;
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 3px;
    }
    .sample-q {
        color: #CBD5E1;
        font-size: 0.9rem;
        font-style: italic;
    }
    .sim-btn {
        display: inline-block;
        background-color: #2563EB;
        color: white !important;
        padding: 8px 16px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.9rem;
        margin-bottom: 10px;
    }
    .sim-btn:hover {
        background-color: #1D4ED8;
    }
    </style>
""", unsafe_allow_html=True)

# 2. State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Helper Function
def render_pcm_response(title, notes_list, sim_url=None, guide_steps=None):
    notes_formatted = "\n".join([f"* {point}" for point in notes_list])
    
    sim_html = ""
    if sim_url and guide_steps:
        guide_formatted = "\n".join([f"{i+1}. {step}" for i, step in enumerate(guide_steps)])
        sim_html = f"""
---
### 🔬 Interactive Visual Simulation
<a href="{sim_url}" target="_blank" class="sim-btn">🔗 Open Full Screen Interactive Tool</a>
<div class="sim-container">
    <iframe src="{sim_url}" allowfullscreen></iframe>
    <div class="brand-overlay"></div>
</div>

**Beginner Guide:**
{guide_formatted}
"""
    return f"""
### {title}

**Key Theory Highlights (Class 12th NCERT):**
{notes_formatted}
{sim_html}
"""

# 3. Router Engine
def get_pcm_response(query):
    text = query.lower()

    # Electrostatics
    if "electrostatic" in text or "charge" in text or "electric field" in text:
        return render_pcm_response(
            "⚡ Electrostatics — Charges & Electric Field",
            [
                "**Coulomb's Law:** Force between two point charges is $F = \\frac{k \\cdot |q_1 q_2|}{r^2}$.",
                "**Electric Field ($E$):** Force per unit positive test charge ($E = \\frac{F}{q}$).",
                "**Electric Dipole Moment ($p$):** Directed from negative to positive charge ($p = q \\times 2a$).",
                "**Gauss's Law:** Total electric flux through a closed surface is $\\frac{Q_{encl}}{\\varepsilon_0}$.",
                "**Equipotential Surfaces:** Surfaces having same potential at every point."
            ],
            "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html",
            [
                "Drag positive or negative charges into the field.",
                "Toggle 'Electric Field' and 'Equipotential' check-boxes.",
                "Place sensors at different distances to measure field strength."
            ]
        )

    # Solenoid
    elif "solenoid" in text:
        return render_pcm_response(
            "🌀 Solenoid & Its Magnetic Field",
            [
                "**Definition:** A long cylindrical coil of insulated copper wire wound in the shape of a helix.",
                "**Internal Field:** Field lines inside are uniform and parallel ($B = \\mu_0 n I$).",
                "**Number Density ($n$):** Represents total turns per unit length ($n = \\frac{N}{L}$).",
                "**External Field:** Magnetic field outside a long solenoid is nearly zero.",
                "**Electromagnet Core:** Soft iron core enhances magnetic field due to high permeability."
            ],
            "https://phet.colorado.edu/sims/html/generator/latest/generator_en.html",
            [
                "Select the Electromagnet / Solenoid tab in the simulation.",
                "Adjust current flow and number of loops on the coil.",
                "Observe magnetic field lines generated inside and around the solenoid."
            ]
        )

    # Faraday's Law / EMI
    elif "induction" in text or "faraday" in text or "emi" in text or "generator" in text:
        return render_pcm_response(
            "⚡ Electromagnetic Induction & Faraday's Laws",
            [
                "**Magnetic Flux ($\\Phi_B$):** Measure of field lines passing through an area ($\\Phi_B = B A \\cos\\theta$).",
                "**Faraday's 1st Law:** Changing magnetic flux induces an electromotive force (EMF).",
                "**Faraday's 2nd Law:** Magnitude of induced EMF is $\\mathcal{E} = -\\frac{d\\Phi_B}{dt}$.",
                "**Lenz's Law:** Induced current opposes the change in magnetic flux that produced it.",
                "**Eddy Currents:** Circulating currents induced in bulk conductors due to changing flux."
            ],
            "https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html",
            [
                "Move the bar magnet through the coil loop.",
                "Observe direction of current flow indicated by the voltmeter.",
                "Observe bulb light intensity relative to magnet speed."
            ]
        )

    # Circuits
    elif "circuit" in text or "ohm" in text or "resistance" in text or "current" in text:
        return render_pcm_response(
            "🔌 Current Electricity & Circuits",
            [
                "**Ohm's Law:** Voltage is directly proportional to current ($V = IR$).",
                "**Drift Velocity ($v_d$):** Average velocity acquired by electrons ($I = n e A v_d$).",
                "**Resistivity ($\\rho$):** Material property defining resistance ($R = \\rho \\frac{L}{A}$).",
                "**Kirchhoff's Current Law:** Total current entering a junction equals current leaving.",
                "**Kirchhoff's Voltage Law:** Algebraic sum of potential changes in a loop is zero."
            ],
            "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html",
            [
                "Drag wires, battery, and resistors onto screen.",
                "Connect components in a closed circuit loop.",
                "Use voltmeter and ammeter tools to test Ohm's Law."
            ]
        )

    # Ray Optics
    elif "lens" in text or "mirror" in text or "optics" in text or "ray" in text:
        return render_pcm_response(
            "🔍 Ray Optics — Lenses & Refraction",
            [
                "**Snell's Law:** $n_1 \\sin i = n_2 \\sin r$.",
                "**Lens Formula:** $\\frac{1}{f} = \\frac{1}{v} - \\frac{1}{u}$.",
                "**Lens Maker's Formula:** $\\frac{1}{f} = (n-1) \\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right)$.",
                "**Power of Lens ($P$):** Reciprocal of focal length in meters ($P = \\frac{1}{f}$).",
                "**Total Internal Reflection:** Occurs when light travels from denser to rarer medium at $i > i_c$."
            ],
            "https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_en.html",
            [
                "Select Convex or Concave lens setup.",
                "Change focal length slider and drag object position.",
                "Trace principal light rays to observe image formation."
            ]
        )

    # Electrochemistry
    elif "electrochemistry" in text or "galvanic" in text or "cell" in text:
        return render_pcm_response(
            "🔋 Electrochemistry & Galvanic Cells",
            [
                "**Galvanic Cell:** Converts chemical energy into electrical energy via redox reaction.",
                "**Anode vs Cathode:** Oxidation occurs at Anode, Reduction occurs at Cathode.",
                "**Nernst Equation:** $E = E^0 - \\frac{RT}{nF} \\ln Q$.",
                "**Kohlrausch's Law:** Limiting molar conductivity is the sum of ionic conductivities.",
                "**Faraday's Law of Electrolysis:** Mass deposited is $m = Z I t$."
            ],
            "https://phet.colorado.edu/sims/html/reactivity/latest/reactivity_en.html",
            [
                "Dip different metal strips into chemical solutions.",
                "Compare electron displacement reactivity series.",
                "Observe ion formation across different metals."
            ]
        )

    # Default Theory
    else:
        return render_pcm_response(
            f"📘 Concept Notes: **{query.title()}**",
            [
                "**NCERT Foundation:** Core Class 12th Board concepts and formulas.",
                "**Definition & Scope:** Covers basic principles, unit dimensions, and key derivations.",
                "**Key Formula:** Standard algebraic and differential textbook equations.",
                "**Applications:** Relevant for Board exams and competitive preparation.",
                "**Exam Tip:** Practice step-by-step numerical problems and derivations."
            ]
        )

# 4. Persistent Home Screen
st.markdown("""
    <div class="title-container">
        <img src="https://img.icons8.com/color/96/sparkling.png" class="logo-img">
        <h1 class="main-title">Ask ChitraVidya AI</h1>
    </div>
""", unsafe_allow_html=True)
st.markdown('<p class="sub-title">Class 12th PCM Interactive Guide</p>', unsafe_allow_html=True)

st.markdown("---")

# 5. Display Chat History
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        if msg["role"] == "user":
            st.markdown(f'<div id="target-latest-msg"></div>', unsafe_allow_html=True)
        st.markdown(msg["content"], unsafe_allow_html=True)

# 6. Chat Input & Auto-Scroll
user_input = st.chat_input("Ask ChitraVidya AI (e.g. 'Explain solenoid')...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    response = get_pcm_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()

# Execute Auto-Scroll to the newly searched response position
st.markdown(
    """
    <script>
        const targetElement = window.parent.document.getElementById('target-latest-msg');
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    </script>
    """,
    unsafe_allow_html=True
)
