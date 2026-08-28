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
    /* Hide the bottom PhET navigation/logo bar by cropping the iframe view */
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
        margin-bottom: -50px; /* Crops out bottom toolbar */
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

# Helper Function to Render Simulation Block safely
def render_sim_block(title, notes, sim_url, guide_steps):
    return f"""
### {title}

**Key Theory Highlights:**
{notes}

---
### 🔬 Topic-Specific Interactive Simulation
<a href="{sim_url}" target="_blank" class="sim-btn">🔗 Open Full Screen Interactive Tool</a>
<div class="sim-container">
    <iframe src="{sim_url}" allowfullscreen></iframe>
</div>

**Beginner Guide:**
{guide_steps}
"""

# 3. Topic-Specific Precise Router Engine
def get_pcm_response(query):
    text = query.lower()

    # ================= PHYSICS =================
    if "electrostatic" in text or "charge" in text or "electric field" in text:
        return render_sim_block(
            "⚡ Electrostatics — Charges & Electric Field",
            "* **Coulomb's Law:** $F = \\frac{k \\cdot |q_1 q_2|}{r^2}$\n* **Electric Field ($E$):** $E = \\frac{F}{q}$ (Force per unit positive test charge).",
            "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html",
            "1. Drag positive (+1nC) or negative (-1nC) charges into the field.\n2. Check 'Electric Field' and 'Equipotential' to visualize field lines.\n3. Place sensors to measure local voltage and field direction."
        )

    elif "circuit" in text or "ohm" in text or "resistance" in text or "current" in text:
        return render_sim_block(
            "🔌 Electric Circuits — Current, Resistance & Ohm’s Law",
            "* **Ohm's Law:** $V = IR$\n* **Equivalent Resistance:** $R_{series} = R_1 + R_2$, $\\frac{1}{R_{parallel}} = \\frac{1}{R_1} + \\frac{1}{R_2}$",
            "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html",
            "1. Drag wires, battery, and resistors onto the canvas.\n2. Connect them in a complete loop.\n3. Use the Voltmeter and Ammeter to verify Ohm's Law ($V = IR$)."
        )

    elif "solenoid" in text or "magnetic field" in text or "electromagnet" in text:
        return render_sim_block(
            "🌀 Solenoid & Electromagnetism",
            "* **Magnetic Field Inside Solenoid:** $B = \\mu_0 n I$\n* Field lines inside a solenoid are uniform and parallel, acting like a bar magnet.",
            "https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html?screens=1",
            "1. Move the bar magnet inside and outside the wire coil (solenoid).\n2. Observe how changing magnetic flux induces electric current.\n3. Check field lines toggle to visualize the magnetic envelope."
        )

    elif "induction" in text or "faraday" in text or "emi" in text or "generator" in text:
        return render_sim_block(
            "⚡ Electromagnetic Induction — Faraday's Law",
            "* **Faraday's Law:** $\\mathcal{E} = -\\frac{d\\Phi_B}{dt}$\n* **Lenz's Law:** Induced current opposes the change in magnetic flux that produces it.",
            "https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html?screens=2",
            "1. Switch to Generator/Pickup Coil screen.\n2. Rotate the water tap/magnet to alter flux density.\n3. Observe AC light bulb intensity changes."
        )

    elif "lens" in text or "mirror" in text or "optics" in text or "ray" in text:
        return render_sim_block(
            "🔍 Ray Optics — Lenses & Refraction",
            "* **Lens Formula:** $\\frac{1}{f} = \\frac{1}{v} - \\frac{1}{u}$\n* **Magnification:** $m = \\frac{v}{u} = \\frac{h_i}{h_o}$",
            "https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_en.html",
            "1. Select Convex or Concave lens.\n2. Change focal length and object position.\n3. Track principal rays to see real/virtual image formation."
        )

    elif "wave" in text or "interference" in text or "diffraction" in text:
        return render_sim_block(
            "🌊 Wave Optics & Wave Motion",
            "* **Wave Equation:** $v = f \\lambda$\n* **Superposition Principle:** Resultant displacement $y = y_1 + y_2$",
            "https://phet.colorado.edu/sims/html/wave-interference/latest/wave-interference_en.html",
            "1. Choose Water, Sound, or Light waves.\n2. Add a second source to observe constructive and destructive interference patterns."
        )

    # ================= CHEMISTRY =================
    elif "electrochemistry" in text or "galvanic" in text or "cell" in text:
        return render_sim_block(
            "🔋 Electrochemistry — Reactivity & Galvanic Cells",
            "* **Standard Cell Potential:** $E^0_{cell} = E^0_{cathode} - E^0_{anode}$\n* Oxidation happens at Anode; Reduction happens at Cathode.",
            "https://phet.colorado.edu/sims/html/reactivity/latest/reactivity_en.html",
            "1. Insert different metal strips into chemical solutions.\n2. Compare electron transfer rates and reactivity series."
        )

    elif "kinetics" in text or "rate" in text or "reaction" in text:
        return render_sim_block(
            "⏱️ Chemical Kinetics — Reaction Rates & Activation Energy",
            "* **Rate Law:** Rate = $k[A]^a [B]^b$\n* **Arrhenius Equation:** $k = A e^{-E_a / RT}$",
            "https://phet.colorado.edu/sims/html/reactions-and-rates/latest/reactions-and-rates_en.html",
            "1. Pump reactants into the reaction vessel.\n2. Adjust heat supply to observe activation energy barriers and collision frequency."
        )

    elif "solution" in text or "molarity" in text or "concentration" in text:
        return render_sim_block(
            "🧪 Solutions — Molarity & Concentration",
            "* **Molarity ($M$):** $M = \\frac{\\text{Moles of Solute}}{\\text{Volume of Solution in Liters}}$\n* **Dilution:** $M_1 V_1 = M_2 V_2$",
            "https://phet.colorado.edu/sims/html/concentration/latest/concentration_en.html",
            "1. Add solute powders or liquids into water.\n2. Read molar concentration meter.\n3. Add water or evaporate to see concentration shifts."
        )

    elif "ph" in text or "acid" in text or "base" in text:
        return render_sim_block(
            "🧪 Acids, Bases & pH Scale",
            "* $\\text{pH} = -\\log_{10}[H^+]$\n* $\\text{pH} < 7$ (Acidic), $\\text{pH} = 7$ (Neutral), $\\text{pH} > 7$ (Basic)",
            "https://phet.colorado.edu/sims/html/ph-scale/latest/ph-scale_en.html",
            "1. Choose liquids like battery acid, coffee, soap, or water.\n2. Dip the pH probe to measure hydrogen ion concentration."
        )

    # ================= MATHEMATICS =================
    elif "derivative" in text or "calculus" in text or "slope" in text:
        return render_sim_block(
            "📈 Application of Derivatives & Calculus",
            "* **Derivative as Rate of Change:** $f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}$\n* Local Maxima/Minima occur where $f'(x) = 0$.",
            "https://www.geogebra.org/graphing?embed",
            "1. Type any function (e.g., `f(x) = x^3 - 3*x`).\n2. Type `Derivative(f)` to automatically plot the tangent slope graph."
        )

    elif "probability" in text or "statistics" in text or "bayes" in text:
        return render_sim_block(
            "🎲 Probability & Distributions",
            "* **Conditional Probability:** $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$\n* **Bayes' Theorem:** $P(A|B) = \\frac{P(B|A)P(A)}{P(B)}$",
            "https://www.geogebra.org/classic/probability?embed",
            "1. Select Binomial, Normal, or Poisson distribution modes.\n2. Adjust $n$ and $p$ parameters to visualize probability curve distributions."
        )

    # ================= SAFE FALLBACK =================
    # If topic does not have a dedicated PhET sim, gracefully open GeoGebra Interactive Visual Canvas
    else:
        return render_sim_block(
            f"📘 Concept Explorer: **{query.title()}**",
            "* Review standard Class 12 NCERT formulas & principles related to this topic.\n* Use the general interactive canvas below for graph plotting and visual modeling.",
            "https://www.geogebra.org/calculator?embed",
            "1. Enter mathematical functions or equations for visual graphing.\n2. Explore geometric and numeric behavior dynamically."
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
        <div class="sample-q">💬 Ask: "Explain electrostatics and charges"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">2. Electric Circuits</div>
        <div class="sample-q">💬 Ask: "Explain electric circuits and Ohm's law"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">3. Solenoid</div>
        <div class="sample-q">💬 Ask: "Explain solenoid magnetic field"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">4. Electromagnetic Induction</div>
        <div class="sample-q">💬 Ask: "Explain Faraday's law and EMI"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">5. Ray Optics</div>
        <div class="sample-q">💬 Ask: "Explain lenses and mirrors in optics"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">6. Wave Optics</div>
        <div class="sample-q">💬 Ask: "Explain wave interference"</div>
    </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown("#### 🧪 Chemistry Topics")
    st.markdown("""
    <div class="topic-card">
        <div class="topic-title">7. Electrochemistry</div>
        <div class="sample-q">💬 Ask: "Explain galvanic cells and electrochemistry"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">8. Chemical Kinetics</div>
        <div class="sample-q">💬 Ask: "Explain chemical kinetics and reaction rate"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">9. Solutions</div>
        <div class="sample-q">💬 Ask: "Explain solutions and molarity"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">10. Acids & Bases</div>
        <div class="sample-q">💬 Ask: "Explain pH scale and acids bases"</div>
    </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown("#### 📐 Mathematics Topics")
    st.markdown("""
    <div class="topic-card">
        <div class="topic-title">11. Application of Derivatives</div>
        <div class="sample-q">💬 Ask: "Explain application of derivatives"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">12. Probability</div>
        <div class="sample-q">💬 Ask: "Explain probability and distributions"</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 5. Display Chat History Below Topics
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
