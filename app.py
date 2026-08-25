import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="ChitraVidya AI | Class 12 PCM",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Clean UI & Layout Structure
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
        overflow: hidden;
        border-radius: 12px;
        border: 1px solid #374151;
        background: #0f172a;
        margin-bottom: 10px;
    }
    .sim-container iframe {
        width: 100%;
        height: 480px;
        border: none;
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
        margin-bottom: 15px;
    }
    .sim-btn:hover {
        background-color: #1D4ED8;
    }
    </style>
""", unsafe_allow_html=True)

# 2. State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Precise PCM Router & Content Engine (Strict Matching)
def get_pcm_response(query):
    text = query.lower()
    
    # ================= PHYSICS =================
    if "electrostatic" in text or "charge" in text or "electric field" in text:
        return """
### ⚡ Electrostatics — Charges & Electric Field

**Key Theory Highlights:**
* **Coulomb's Law:** $F = \\frac{k \\cdot |q_1 q_2|}{r^2}$
* **Electric Field ($E$):** Force experienced per unit positive test charge ($E = \\frac{F}{q}$).

---
### 🔬 Interactive Simulation
<a href="https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html" target="_blank" class="sim-btn">🔗 Click to Open Simulation in Full Screen</a>
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html"></iframe>
</div>

**Beginner Guide:**
1. Drag positive or negative charges onto the play area.
2. Use the sensor to measure electric field strength and direction.
"""

    elif "circuit" in text or "ohm" in text or "resistance" in text or "current" in text:
        return """
### 🔌 Electric Circuits — Current, Resistance, Ohm’s Law

**Key Theory Highlights:**
* **Ohm's Law:** $V = IR$ (Voltage = Current $\\times$ Resistance).
* **Series vs Parallel:** Understanding equivalent resistance in circuits.

---
### 🔬 Interactive Simulation
<a href="https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html" target="_blank" class="sim-btn">🔗 Click to Open Simulation in Full Screen</a>
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html"></iframe>
</div>

**Beginner Guide:**
1. Drag wires, batteries, and resistors into the workspace.
2. Connect them together to form a closed loop and observe current flow.
"""

    elif "solenoid" in text:
        return """
### 🌀 Solenoid — Magnetic Field & Electromagnets

**Key Theory Highlights:**
* **Solenoid Field:** $B = \\mu_0 n I$ (Uniform magnetic field inside a long current-carrying coil).
* Magnetic field lines inside are parallel and strong, while outside they are nearly zero.

---
### 🔬 Interactive Simulation
<a href="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html?screens=1" target="_blank" class="sim-btn">🔗 Click to Open Simulation in Full Screen</a>
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html?screens=1"></iframe>
</div>

**Beginner Guide:**
1. Move the bar magnet in and out of the coil.
2. Observe how the magnetic flux change produces a current and lights up the bulb.
"""

    elif "magnet" in text or "electromagnet" in text:
        return """
### 🧲 Magnetism — Magnetic Field & Electromagnets

**Key Theory Highlights:**
* Magnetic field lines form continuous closed loops from North to South pole.
* Electromagnet strength increases with number of turns and current.

---
### 🔬 Interactive Simulation
<a href="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html?screens=1" target="_blank" class="sim-btn">🔗 Click to Open Simulation in Full Screen</a>
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html?screens=1"></iframe>
</div>

**Beginner Guide:**
1. Check the magnetic field lines option.
2. Move the compass around the magnet to check field directions.
"""

    elif "induction" in text or "faraday" in text or "generator" in text or "emi" in text:
        return """
### ⚡ Electromagnetic Induction — Faraday’s Law, Generator

**Key Theory Highlights:**
* **Faraday's Law:** $\\mathcal{E} = -\\frac{d\\Phi_B}{dt}$ (Induced EMF depends on rate of change of magnetic flux).
* **Lenz's Law:** Induced current opposes the change producing it.

---
### 🔬 Interactive Simulation
<a href="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html?screens=2" target="_blank" class="sim-btn">🔗 Click to Open Simulation in Full Screen</a>
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html?screens=2"></iframe>
</div>

**Beginner Guide:**
1. Rotate the loop inside the magnetic field to generate electricity.
2. Observe AC voltage variations on the oscilloscope screen.
"""

    elif "lens" in text or "mirror" in text or "optics" in text:
        return """
### 🔍 Ray Optics — Lenses & Mirrors

**Key Theory Highlights:**
* **Mirror Formula:** $\\frac{1}{f} = \\frac{1}{v} + \\frac{1}{u}$
* **Lens Formula:** $\\frac{1}{f} = \\frac{1}{v} - \\frac{1}{u}$

---
### 🔬 Interactive Simulation
<a href="https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_en.html" target="_blank" class="sim-btn">🔗 Click to Open Simulation in Full Screen</a>
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_en.html"></iframe>
</div>

**Beginner Guide:**
1. Place an object in front of a convex/concave lens.
2. Adjust focal length and object distance to see real or virtual images.
"""


    # ================= CHEMISTRY =================
    elif "electrochemistry" in text or "galvanic" in text or "cell" in text:
        return """
### 🔋 Electrochemistry — Galvanic Cells, Voltage

**Key Theory Highlights:**
* **Cell Potential:** $E_{cell} = E_{cathode} - E_{anode}$
* Oxidation takes place at anode and reduction at cathode.

---
### 🔬 Interactive Simulation
<a href="https://phet.colorado.edu/sims/html/reactivity/latest/reactivity_en.html" target="_blank" class="sim-btn">🔗 Click to Open Simulation in Full Screen</a>
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/reactivity/latest/reactivity_en.html"></iframe>
</div>

**Beginner Guide:**
1. Select different metals and place them in salt solutions.
2. Compare reactivity and observe voltage generated in the cell.
"""

    elif "kinetics" in text or "reaction rate" in text or "concentration" in text:
        return """
### ⏱️ Chemical Kinetics — Reaction Rate & Concentration

**Key Theory Highlights:**
* **Rate Law:** Rate = $k[A]^x[B]^y$
* Higher concentration or temperature increases collision frequency and reaction rate.

---
### 🔬 Interactive Simulation
<a href="https://phet.colorado.edu/sims/html/reactions-and-rates/latest/reactions-and-rates_en.html" target="_blank" class="sim-btn">🔗 Click to Open Simulation in Full Screen</a>
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/reactions-and-rates/latest/reactions-and-rates_en.html"></iframe>
</div>

**Beginner Guide:**
1. Pump reactant molecules into the chamber.
2. Adjust temperature and initial amounts to track product formation over time.
"""

    elif "solution" in text or "molarity" in text or "dilution" in text:
        return """
### 🧪 Solutions — Concentration, Molarity, Dilution

**Key Theory Highlights:**
* **Molarity ($M$):** Moles of solute per liter of solution.
* **Dilution rule:** $M_1V_1 = M_2V_2$

---
### 🔬 Interactive Simulation
<a href="https://phet.colorado.edu/sims/html/concentration/latest/concentration_en.html" target="_blank" class="sim-btn">🔗 Click to Open Simulation in Full Screen</a>
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/concentration/latest/concentration_en.html"></iframe>
</div>

**Beginner Guide:**
1. Add solute or solvent to change solution concentration.
2. Use the concentration meter to measure molarity.
"""

    elif "ph" in text or "acid" in text or "base" in text or "indicator" in text:
        return """
### 🧪 Acids & Bases — pH and Indicators

**Key Theory Highlights:**
* $\\text{pH} = -\\log[H^+]$
* Acidic solutions ($\\text{pH} < 7$), Basic solutions ($\\text{pH} > 7$).

---
### 🔬 Interactive Simulation
<a href="https://phet.colorado.edu/sims/html/ph-scale/latest/ph-scale_en.html" target="_blank" class="sim-btn">🔗 Click to Open Simulation in Full Screen</a>
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/ph-scale/latest/ph-scale_en.html"></iframe>
</div>

**Beginner Guide:**
1. Use the dropper to add different liquids (coffee, soap, water) to the beaker.
2. Dip the pH sensor to check exact acidic or basic nature.
"""

    elif "surface chemistry" in text or "adsorption" in text or "colloid" in text:
        return """
### ⚗️ Surface Chemistry — Adsorption / Colloids

**Key Theory Highlights:**
* **Adsorption:** Accumulation of molecular species at the surface rather than in the bulk.
* Lyophilic and Lyophobic colloids show Tyndall effect.

---
### 🔬 Interactive Simulation
<a href="https://phet.colorado.edu/sims/html/states-of-matter-basics/latest/states-of-matter-basics_en.html" target="_blank" class="sim-btn">🔗 Click to Open Simulation in Full Screen</a>
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/states-of-matter-basics/latest/states-of-matter-basics_en.html"></iframe>
</div>

**Beginner Guide:**
1. Heat or cool atoms/molecules to observe phase changes.
2. Analyze surface interactions and particle behavior.
"""


    # ================= MATHEMATICS =================
    elif "derivative" in text or "application of derivatives" in text or "rate of change" in text:
        return """
### 📈 Application of Derivatives

**Key Theory Highlights:**
* Rate of change of quantities, increasing/decreasing functions, tangents and normals.
* Finding local maxima and minima using first and second derivative tests.

---
### 📐 Interactive Canvas
<a href="https://www.geogebra.org/graphing?embed" target="_blank" class="sim-btn">🔗 Click to Open Calculator in Full Screen</a>
<div class="sim-container">
    <iframe src="https://www.geogebra.org/graphing?embed"></iframe>
</div>

**Beginner Guide:**
1. Type functions like `f(x) = x^3 - 3x` in the input bar.
2. Find turning points and slopes directly on the graph.
"""

    elif "probability" in text or "bayes" in text or "conditional" in text:
        return """
### 🎲 Probability

**Key Theory Highlights:**
* Conditional probability: $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$
* Bayes' Theorem and Probability Distributions.

---
### 📐 Interactive Canvas
<a href="https://www.geogebra.org/scientific?embed" target="_blank" class="sim-btn">🔗 Click to Open Tool in Full Screen</a>
<div class="sim-container">
    <iframe src="https://www.geogebra.org/scientific?embed"></iframe>
</div>

**Beginner Guide:**
1. Use scientific tools for quick statistical calculations and permutations.
"""


    # --- FALLBACK / DEFAULT WELCOME SCREEN ---
    else:
        return f"""
### 📘 ChitraVidya AI: **{query.title()}**

Please type any of the exact topics listed on the home screen to view its theory notes and interactive simulation!
"""

# 4. Persistent Home Screen (Visible Always at the Top)
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
        <div class="topic-title">4. Magnetism</div>
        <div class="sample-q">💬 Ask: "Explain magnetism and electromagnets"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">5. Electromagnetic Induction</div>
        <div class="sample-q">💬 Ask: "Explain Faraday's law and EMI"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">6. Ray Optics</div>
        <div class="sample-q">💬 Ask: "Explain lenses and mirrors in optics"</div>
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
    <div class="topic-card">
        <div class="topic-title">11. Surface Chemistry</div>
        <div class="sample-q">💬 Ask: "Explain adsorption and surface chemistry"</div>
    </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown("#### 📐 Mathematics Topics")
    st.markdown("""
    <div class="topic-card">
        <div class="topic-title">12. Application of Derivatives</div>
        <div class="sample-q">💬 Ask: "Explain application of derivatives"</div>
    </div>
    <div class="topic-card">
        <div class="topic-title">13. Probability</div>
        <div class="sample-q">💬 Ask: "Explain probability and conditional probability"</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 5. Display Chat History Below Topics
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

# 6. Bottom Chat Input
user_input = st.chat_input("Ask ChitraVidya AI (e.g. 'Explain solenoid')...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate structured response
    response = get_pcm_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()
