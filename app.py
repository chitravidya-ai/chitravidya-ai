import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="ChitraVidya AI | Class 12 PCM",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS: Hide PhET branding, settings icon & 3-dots on right bottom
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
    /* Extended Overlay box hiding PhET Logo, Settings Gear & 3 Dots */
    .brand-overlay {
        position: absolute;
        bottom: 0;
        right: 0;
        width: 180px;
        height: 50px;
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

    # EM Waves (New Topic Added)
    elif "em wave" in text or "electromagnetic wave" in text or "emw" in text:
        return render_pcm_response(
            "🌊 Electromagnetic Waves (EM Waves)",
            [
                "**Nature of EM Waves:** Transverse non-mechanical waves produced by accelerating electric charges.",
                "**Perpendicular Oscillations:** Electric vector ($E$) and Magnetic vector ($B$) oscillate perpendicular to each other and to propagation direction ($c = \\frac{E_0}{B_0}$).",
                "**Speed of Light:** Speed in vacuum is given by $c = \\frac{1}{\\sqrt{\\mu_0 \\varepsilon_0}} \\approx 3 \\times 10^8 \\text{ m/s}$.",
                "**Displacement Current ($I_d$):** Current due to changing electric flux: $I_d = \\varepsilon_0 \\frac{d\\Phi_E}{dt}$.",
                "**Electromagnetic Spectrum:** Radio waves $\\rightarrow$ Microwaves $\\rightarrow$ Infrared $\\rightarrow$ Visible $\\rightarrow$ UV $\\rightarrow$ X-rays $\\rightarrow$ Gamma rays."
            ],
            "https://phet.colorado.edu/sims/html/wave-interference/latest/wave-interference_en.html",
            [
                "Select the Light tab in the simulation.",
                "Adjust frequency and amplitude sliders.",
                "Observe transverse wave oscillations and wave fronts."
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

    # Electrochemistry (Fixed Exact Matching)
    elif "electrochemistry" in text or "galvanic" in text or "cell" in text or "electrochemical" in text:
        return render_pcm_response(
            "🔋 Electrochemistry & Galvanic Cells",
            [
                "**Galvanic Cell:** Converts chemical energy into electrical energy via spontaneous redox reactions.",
                "**Anode vs Cathode:** Oxidation occurs at Anode (Negative electrode), Reduction occurs at Cathode (Positive electrode).",
                "**Nernst Equation:** Calculates cell potential under non-standard conditions: $E_{cell} = E^0_{cell} - \\frac{RT}{nF} \\ln Q$.",
                "**Kohlrausch's Law:** Limiting molar conductivity of an electrolyte is sum of individual ionic conductivities.",
                "**Faraday's Law of Electrolysis:** Mass of substance deposited at an electrode is $m = Z I t$."
            ],
            "https://phet.colorado.edu/sims/html/reactivity/latest/reactivity_en.html",
            [
                "Dip different metal strips into chemical solutions.",
                "Compare electron displacement reactivity series.",
                "Observe ion formation across different metals."
            ]
        )

    # Solutions (Fixed Exact Matching)
    elif "solution" in text or "molarity" in text or "concentration" in text or "dilution" in text:
        return render_pcm_response(
            "🧪 Solutions & Concentration Terms",
            [
                "**Molarity ($M$):** Moles of solute per liter of solution ($M = \\frac{n_{solute}}{V(L)}$).",
                "**Molality ($m$):** Moles of solute per kg of solvent ($m = \\frac{n_{solute}}{W_{solvent}(kg)}$).",
                "**Raoult's Law:** Partial vapor pressure of solvent is proportional to its mole fraction ($p_1 = x_1 p_1^0$).",
                "**Colligative Properties:** Properties depending on number of solute particles (e.g., Osmotic Pressure $\\Pi = CRT$).",
                "**Van 't Hoff Factor ($i$):** Accounts for association or dissociation of solute particles ($i = \\frac{\\text{Observed Property}}{\\text{Theoretical Property}}$)."
            ],
            "https://phet.colorado.edu/sims/html/concentration/latest/concentration_en.html",
            [
                "Add solute powders or liquids into water container.",
                "Dip the concentration probe to measure molarity value.",
                "Evaporate water or add solvent to observe concentration shifts."
            ]
        )

    # Chemical Kinetics
    elif "kinetics" in text or "rate of reaction" in text:
        return render_pcm_response(
            "⏱️ Chemical Kinetics & Reaction Rates",
            [
                "**Rate of Reaction:** Change in concentration of reactants/products per unit time.",
                "**Rate Law:** Mathematical equation relating rate to reactant concentrations ($Rate = k[A]^x[B]^y$).",
                "**Half-Life ($t_{1/2}$):** Time taken for concentration to reduce to half (For 1st order: $t_{1/2} = \\frac{0.693}{k}$).",
                "**Arrhenius Equation:** Describes temperature dependence: $k = A e^{-E_a / RT}$.",
                "**Activation Energy ($E_a$):** Minimum energy required for reactants to form transition complex."
            ],
            "https://phet.colorado.edu/sims/html/reactions-and-rates/latest/reactions-and-rates_en.html",
            [
                "Pump reactant molecules into the reaction chamber.",
                "Adjust temperature slider to view kinetic changes.",
                "Observe collision energy barriers."
            ]
        )

    # Application of Derivatives
    elif "derivative" in text or "calculus" in text:
        return render_pcm_response(
            "📈 Application of Derivatives",
            [
                "**Rate of Change:** Derivative $\\frac{dy}{dx}$ represents instantaneous rate of change.",
                "**Tangents & Normals:** Slope of tangent to curve $y=f(x)$ is $m = \\frac{dy}{dx}$.",
                "**Increasing/Decreasing Functions:** $f(x)$ is strictly increasing if $f'(x) > 0$.",
                "**First Derivative Test:** Critical point $x=c$ is local maxima if $f'(x)$ changes sign from positive to negative.",
                "**Second Derivative Test:** If $f'(c) = 0$ and $f''(c) < 0$, point $c$ is local maximum."
            ],
            "https://www.geogebra.org/graphing?embed",
            [
                "Type function equation like `f(x) = x^3 - 3*x` in input box.",
                "Type `Derivative(f)` to graph slope behavior.",
                "Locate turning points and critical values directly."
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

# 4. Persistent Home Screen with Topics List and Sample Questions
st.markdown("""
    <div class="title-container">
        <img src="https://img.icons8.com/color/96/sparkling.png" class="logo-img">
        <h1 class="main-title">Ask ChitraVidya AI</h1>
    </div>
""", unsafe_allow_html=True)
st.markdown('<p class="sub-title">Class 12th PCM Interactive Guide</p>', unsafe_allow_html=True)

st.markdown("### 📚 Available Topics & How to Ask:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### ⚡ Physics Topics")
    st.markdown("""
    <div class="topic-card">
        <div class="topic-title">1. Electrostatics</div>
        <div class="sample-q">💬 Ask: "Explain electrostatics"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">2. Electric Circuits</div>
        <div class="sample-q">💬 Ask: "Explain electric circuits"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">3. Solenoid</div>
        <div class="sample-q">💬 Ask: "Explain solenoid"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">4. Electromagnetic Induction</div>
        <div class="sample-q">💬 Ask: "Explain Faraday's law"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">5. EM Waves</div>
        <div class="sample-q">💬 Ask: "Explain EM waves"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">6. Ray Optics</div>
        <div class="sample-q">💬 Ask: "Explain optics and lenses"</div>
    </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown("#### 🧪 Chemistry Topics")
    st.markdown("""
    <div class="topic-card">
        <div class="topic-title">7. Electrochemistry</div>
        <div class="sample-q">💬 Ask: "Explain electrochemistry"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">8. Chemical Kinetics</div>
        <div class="sample-q">💬 Ask: "Explain chemical kinetics"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">9. Solutions</div>
        <div class="sample-q">💬 Ask: "Explain solutions and molarity"</div>
    </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown("#### 📐 Mathematics Topics")
    st.markdown("""
    <div class="topic-card">
        <div class="topic-title">10. Application of Derivatives</div>
        <div class="sample-q">💬 Ask: "Explain derivatives"</div>
    </div>
    """, unsafe_allow_html=True)

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

# Auto-Scroll Script Execution
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
