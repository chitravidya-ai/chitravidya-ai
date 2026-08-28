import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="ChitraVidya AI | Class 12 PCM",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Clean UI & Hiding PhET Footer Bar completely
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
        height: 450px;
        overflow: hidden;
        border-radius: 12px;
        border: 1px solid #374151;
        background: #0f172a;
        margin-bottom: 10px;
    }
    .sim-container iframe {
        width: 100%;
        height: 530px;
        border: none;
        margin-bottom: -50px; /* Crops out bottom toolbar cleanly */
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

# Helper Function to Render Response with Option to Include or Omit Simulation
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

# 3. Topic-Specific Router Engine (5 Detailed Points Each + Clean URLs)
def get_pcm_response(query):
    text = query.lower()

    # ================= PHYSICS =================
    if "electrostatic" in text or "charge" in text or "field" in text:
        return render_pcm_response(
            "⚡ Electrostatics — Charges & Electric Field",
            [
                "**Coulomb's Law:** Force between two point charges is directly proportional to product of charges and inversely proportional to square of distance: $F = \\frac{k \\cdot |q_1 q_2|}{r^2}$.",
                "**Electric Field ($E$):** Defined as electric force per unit positive test charge ($E = \\frac{F}{q}$). Its SI unit is N/C or V/m.",
                "**Electric Dipole Moment ($p$):** Measure of separation of equal and opposite charges ($p = q \\times 2a$), directed from negative to positive charge.",
                "**Gauss's Law:** Total electric flux through any closed surface is $\\frac{1}{\\varepsilon_0}$ times total enclosed charge ($ \\oint E \\cdot dA = \\frac{Q_{encl}}{\\varepsilon_0} $).",
                "**Equipotential Surfaces:** Surfaces having same electric potential at every point; electric field lines are always perpendicular to equipotential surfaces."
            ],
            "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html",
            [
                "Drag positive (+1nC) or negative (-1nC) charges into the field.",
                "Toggle 'Electric Field' and 'Equipotential' check-boxes to visualize field vectors.",
                "Place sensors at different distances to measure exact field strength and direction."
            ]
        )

    elif "solenoid" in text:
        # Solenoid Specific (Pure Theory & Clean Working Sim)
        return render_pcm_response(
            "🌀 Solenoid & Its Magnetic Field",
            [
                "**Definition:** A solenoid is a long cylindrical coil of insulated copper wire wound closely in the shape of a helix.",
                "**Internal Magnetic Field:** Inside a long current-carrying solenoid, magnetic field lines are straight, parallel, and uniform ($B = \\mu_0 n I$).",
                "**Number Density ($n$):** Here $n = \\frac{N}{L}$ represents total turns per unit length of the solenoid.",
                "**External Field Behavior:** Magnetic field outside a long solenoid is almost zero because field lines spread over a large volume.",
                "**Electromagnet Core:** Inserting a soft iron core inside the solenoid greatly enhances magnetic field strength due to high magnetic permeability."
            ],
            "https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html",
            [
                "Move the bar magnet through the center of wire coil loops (solenoid).",
                "Observe magnetic flux lines inside coil loops.",
                "Check how changing current/movement induces field response."
            ]
        )

    elif "induction" in text or "faraday" in text or "emi" in text or "generator" in text:
        # Faraday's Law Specific
        return render_pcm_response(
            "⚡ Electromagnetic Induction & Faraday's Laws",
            [
                "**Magnetic Flux ($\\Phi_B$):** Measure of total magnetic field lines passing normally through a surface area ($\\Phi_B = B \\cdot A \\cdot \\cos\\theta$).",
                "**Faraday's 1st Law:** Whenever magnetic flux linked with a closed circuit changes, an electromotive force (EMF) is induced in it.",
                "**Faraday's 2nd Law:** Magnitude of induced EMF is directly proportional to rate of change of magnetic flux ($\\mathcal{E} = -\\frac{d\\Phi_B}{dt}$).",
                "**Lenz's Law:** Direction of induced current is such that it opposes the change in magnetic flux that produced it (Conservation of Energy).",
                "**Eddy Currents:** Induced circulating currents formed in bulk conductors when exposed to changing magnetic flux, causing heat energy loss."
            ],
            "https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html",
            [
                "Move the bar magnet faster or slower into the coil loop.",
                "Observe direction of current flow indicated by voltmeter needle.",
                "Notice how bulb light intensity correlates with speed of magnet motion."
            ]
        )

    elif "circuit" in text or "ohm" in text or "resistance" in text or "current" in text:
        return render_pcm_response(
            "🔌 Current Electricity & Circuits",
            [
                "**Ohm's Law:** Current flowing through a conductor is directly proportional to potential difference across it ($V = IR$) at constant temperature.",
                "**Drift Velocity ($v_d$):** Average velocity acquired by free electrons in a conductor under electric field ($I = n e A v_d$).",
                "**Resistivity ($\\rho$):** Material property defining resistance ($R = \\rho \\frac{L}{A}$), depends on temperature and conductor material.",
                "**Kirchhoff's Current Law (KCL):** Total current entering a junction equals total current leaving (Charge Conservation).",
                "**Kirchhoff's Voltage Law (KVL):** Algebraic sum of potential changes around any closed loop is zero (Energy Conservation)."
            ],
            "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html",
            [
                "Drag wires, battery, and resistors onto screen.",
                "Connect components in a closed circuit loop.",
                "Use voltmeter and ammeter tools to test Ohm's Law ($V = IR$)."
            ]
        )

    elif "lens" in text or "mirror" in text or "optics" in text or "ray" in text:
        return render_pcm_response(
            "🔍 Ray Optics — Lenses & Refraction",
            [
                "**Snell's Law of Refraction:** Ratio of sine of angle of incidence to sine of refraction is constant ($n_1 \\sin i = n_2 \\sin r$).",
                "**Lens Formula:** Relation between object distance ($u$), image distance ($v$), and focal length ($f$): $\\frac{1}{f} = \\frac{1}{v} - \\frac{1}{u}$.",
                "**Lens Maker's Formula:** Formula used by lens manufacturers: $\\frac{1}{f} = (n-1) \\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right)$.",
                "**Power of Lens ($P$):** Reciprocal of focal length in meters ($P = \\frac{1}{f(m)}$), measured in Dioptres (D).",
                "**Total Internal Reflection (TIR):** Occurs when light travels from denser to rarer medium at angle greater than critical angle ($i > i_c$)."
            ],
            "https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_en.html",
            [
                "Select Convex or Concave lens setup.",
                "Change focal length slider and drag object position.",
                "Trace principal light rays to observe real vs virtual image formation."
            ]
        )

    # ================= CHEMISTRY =================
    elif "electrochemistry" in text or "galvanic" in text or "cell" in text:
        return render_pcm_response(
            "🔋 Electrochemistry & Galvanic Cells",
            [
                "**Galvanic (Voltaic) Cell:** Electrochemical device that converts chemical energy from spontaneous redox reactions into electrical energy.",
                "**Anode vs Cathode:** Oxidation occurs at Anode (negative electrode) while Reduction occurs at Cathode (positive electrode).",
                "**Nernst Equation:** Gives cell potential under non-standard conditions: $E = E^0 - \\frac{RT}{nF} \\ln Q$.",
                "**Kohlrausch's Law:** Limiting molar conductivity of an electrolyte is sum of individual ionic conductivities.",
                "**Faraday's 1st Law of Electrolysis:** Mass of substance deposited at an electrode is directly proportional to electric charge passed ($m = Z I t$)."
            ],
            "https://phet.colorado.edu/sims/html/reactivity/latest/reactivity_en.html",
            [
                "Dip different metal strips into chemical solutions.",
                "Compare electron displacement reactivity series.",
                "Observe ion formation across different metals."
            ]
        )

    elif "kinetics" in text or "rate" in text or "reaction" in text:
        return render_pcm_response(
            "⏱️ Chemical Kinetics & Reaction Rates",
            [
                "**Rate of Reaction:** Change in concentration of reactants or products per unit time ($\\text{Rate} = -\\frac{d[R]}{dt} = \\frac{d[P]}{dt}$).",
                "**Rate Law & Order:** Mathematical relation connecting rate to reactant concentrations ($Rate = k[A]^x[B]^y$).",
                "**Half-Life ($t_{1/2}$):** Time required for reactant concentration to reduce to half its initial value (For 1st order: $t_{1/2} = \\frac{0.693}{k}$).",
                "**Arrhenius Equation:** Temperature dependence of rate constant: $k = A e^{-E_a / RT}$.",
                "**Activation Energy ($E_a$):** Minimum energy barrier that reactant molecules must overcome to form transition complex."
            ],
            "https://phet.colorado.edu/sims/html/reactions-and-rates/latest/reactions-and-rates_en.html",
            [
                "Pump reactant molecules into reaction chamber.",
                "Increase or decrease temperature slider.",
                "Observe energy barrier and collision frequency graphs."
            ]
        )

    elif "solution" in text or "molarity" in text or "concentration" in text:
        return render_pcm_response(
            "🧪 Solutions & Concentration Terms",
            [
                "**Molarity ($M$):** Number of moles of solute dissolved per liter of solution ($M = \\frac{n}{V(L)}$).",
                "**Molality ($m$):** Number of moles of solute per kilogram of solvent ($m = \\frac{n}{W_{solvent}(kg)}$).",
                "**Raoult's Law:** Relative lowering of vapor pressure of ideal solution equals mole fraction of non-volatile solute.",
                "**Colligative Properties:** Properties depending only on number of solute particles (e.g., Osmotic Pressure $\\Pi = CRT$).",
                "**Van 't Hoff Factor ($i$):** Ratio of experimental colligative property value to calculated theoretical value ($i = \\frac{\\text{Observed}}{\\text{Calculated}}$)."
            ],
            "https://phet.colorado.edu/sims/html/concentration/latest/concentration_en.html",
            [
                "Add solute salt powders or liquid concentrates into water container.",
                "Read exact molarity value on concentration meter probe.",
                "Evaporate water or add solvent to observe molarity changes."
            ]
        )

    # ================= MATHEMATICS =================
    elif "derivative" in text or "calculus" in text:
        return render_pcm_response(
            "📈 Application of Derivatives",
            [
                "**Rate of Change:** Derivative $\\frac{dy}{dx}$ represents instantaneous rate of change of $y$ with respect to $x$.",
                "**Tangents & Normals:** Slope of tangent to curve $y=f(x)$ at $(x_1, y_1)$ is $m = \\left(\\frac{dy}{dx}\\right)_{(x_1, y_1)}$.",
                "**Increasing/Decreasing Functions:** $f(x)$ is strictly increasing if $f'(x) > 0$ and strictly decreasing if $f'(x) < 0$.",
                "**First Derivative Test:** Critical point $x=c$ is local maxima if $f'(x)$ changes sign from positive to negative as $x$ increases.",
                "**Second Derivative Test:** If $f'(c) = 0$ and $f''(c) < 0$, point $c$ is local maximum; if $f''(c) > 0$, it is local minimum."
            ],
            "https://www.geogebra.org/graphing?embed",
            [
                "Type function equation like `f(x) = x^3 - 3*x` in input box.",
                "Type `Derivative(f)` to graph slope behavior.",
                "Locate turning points and critical values directly."
            ]
        )

    # ================= TOPIC WITHOUT PHET SIMULATION (THEORY ONLY) =================
    else:
        # Custom NCERT Theory Only (No Broken Iframe/Error Popup)
        return render_pcm_response(
            f"📘 Concept Notes: **{query.title()}**",
            [
                "**NCERT Foundation:** This topic covers core Class 12th Board principles and standard numerical formulas.",
                "**Definition & Scope:** Focuses on fundamental definitions, unit dimensions, and core derivations.",
                "**Key Formula:** Review relevant governing differential or algebraic equations from your textbook.",
                "**Important Applications:** Frequently asked in competitive exams like JEE/NEET and Board subjective questions.",
                "**Exam Tip:** Practice step-by-step numerical problems and boundary condition derivations for full marks."
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
        <div class="topic-title">5. Ray Optics</div>
        <div class="sample-q">💬 Ask: "Explain optics and lenses"</div>
    </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown("#### 🧪 Chemistry Topics")
    st.markdown("""
    <div class="topic-card">
        <div class="topic-title">6. Electrochemistry</div>
        <div class="sample-q">💬 Ask: "Explain electrochemistry"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">7. Chemical Kinetics</div>
        <div class="sample-q">💬 Ask: "Explain chemical kinetics"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">8. Solutions</div>
        <div class="sample-q">💬 Ask: "Explain solutions and molarity"</div>
    </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown("#### 📐 Mathematics Topics")
    st.markdown("""
    <div class="topic-card">
        <div class="topic-title">9. Application of Derivatives</div>
        <div class="sample-q">💬 Ask: "Explain derivatives"</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 5. Display Chat History
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        if msg["role"] == "user":
            st.markdown(f'<div id="msg-{i}"></div>', unsafe_allow_html=True)
        st.markdown(msg["content"], unsafe_allow_html=True)

# 6. Bottom Chat Input
user_input = st.chat_input("Ask ChitraVidya AI (e.g. 'Explain solenoid')...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    response = get_pcm_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    new_index = len(st.session_state.messages) - 2
    st.markdown(
        f"""
        <script>
            const targetElement = window.parent.document.getElementById('msg-{new_index}');
            if (targetElement) {{
                targetElement.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
            }}
        </script>
        """,
        unsafe_allow_html=True
    )
    
    st.rerun()
