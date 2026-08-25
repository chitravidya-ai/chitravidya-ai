import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="ChitraVidya AI | Class 12 PCM",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Clean UI & Auto-scrolling fix
st.markdown("""
    <style>
    .title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        margin-top: 5vh;
        margin-bottom: 0px;
    }
    .logo-img {
        width: 55px;
        height: 55px;
        border-radius: 50%;
        object-fit: cover;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(45deg, #4F46E5, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .sub-title {
        text-align: center;
        font-size: 1.3rem;
        color: #9CA3AF;
        margin-bottom: 3rem;
        font-weight: 500;
    }
    .sim-container iframe {
        width: 100%;
        height: 520px;
        border: 1px solid #374151;
        border-radius: 12px;
    }
    .suggestion-box {
        background-color: #1F2937;
        padding: 12px 18px;
        border-radius: 8px;
        border-left: 4px solid #06B6D4;
        margin-bottom: 15px;
        color: #E5E7EB;
    }
    </style>
""", unsafe_allow_html=True)

# 2. State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Precise PCM Router & Content Engine with Suggested Questions
def get_pcm_response(query):
    text = query.lower()
    
    # --- PHYSICS 1: Electrostatics ---
    if any(k in text for k in ["electrostatics", "charges", "electric field", "charge"]):
        return """
### ⚡ Electrostatics — Charges & Electric Field

<div class="suggestion-box">
<strong>💡 Aap aise questions puch sakte hain:</strong><br>
• "Explain electric field lines between two positive charges."<br>
• "How does distance affect the electrostatic force between charges?"
</div>

**Key Theory Highlights:**
* **Coulomb's Law:** $F = \\frac{1}{4\\pi\\varepsilon_0} \\frac{q_1 q_2}{r^2}$.
* Electric field lines originate from positive charges and terminate on negative charges.

---
### 🔬 Interactive Field & Charge Visualizer
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/electric-field-hockey/latest/electric-field-hockey_en.html"></iframe>
</div>
"""

    # --- PHYSICS 2: Electric Circuits ---
    elif any(k in text for k in ["circuit", "ohm", "resistance", "current"]):
        return """
### 🔌 Electric Circuits — Current, Resistance, Ohm’s Law

<div class="suggestion-box">
<strong>💡 Aap aise questions puch sakte hain:</strong><br>
• "What is Ohm's Law and how does resistance affect current?"<br>
• "How to connect a simple DC circuit with a bulb and battery?"
</div>

**Key Theory Highlights:**
* **Ohm's Law:** $V = IR$.
* Equivalent resistance in series ($R = R_1 + R_2$) and parallel ($\\frac{1}{R} = \\frac{1}{R_1} + \\frac{1}{R_2}$).

---
### 🔬 Interactive Circuit Construction Kit
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html"></iframe>
</div>
"""

    # --- PHYSICS 3: Magnetism ---
    elif any(k in text for k in ["magnet", "solenoid", "electromagnet", "magnetic field"]):
        return """
### 🧲 Magnetism — Magnetic Field & Electromagnets

<div class="suggestion-box">
<strong>💡 Aap aise questions puch sakte hain:</strong><br>
• "What is the magnetic field pattern inside a current-carrying solenoid?"<br>
• "How does changing current strength affect an electromagnet?"
</div>

**Key Theory Highlights:**
* Solenoid magnetic field: $B = \\mu_0 n I$.
* Magnetic field lines form continuous closed loops from North to South outside, and South to North inside.

---
### 🔬 Interactive Magnetic Field Lab
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html?screens=1"></iframe>
</div>
"""

    # --- PHYSICS 4: Electromagnetic Induction ---
    elif any(k in text for k in ["induction", "faraday", "generator", "emi", "lenz"]):
        return """
### ⚡ Electromagnetic Induction — Faraday’s Law, Generator

<div class="suggestion-box">
<strong>💡 Aap aise questions puch sakte hain:</strong><br>
• "State Faraday's Law of Electromagnetic Induction."<br>
• "How does a bar magnet moving through a coil produce electric current?"
</div>

**Key Theory Highlights:**
* **Faraday's Law:** Induced EMF $\\mathcal{E} = -\\frac{d\\Phi}{dt}$.
* **Lenz's Law:** Direction of induced current always opposes the change producing it.

---
### 🔬 Interactive Induction Generator
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html?screens=1"></iframe>
</div>
"""

    # --- PHYSICS 5: Ray Optics ---
    elif any(k in text for k in ["optics", "lens", "mirror", "refraction", "reflection"]):
        return """
### 👓 Ray Optics — Lenses & Mirrors

<div class="suggestion-box">
<strong>💡 Aap aise questions puch sakte hain:</strong><br>
• "What is the lens maker's formula?"<br>
• "How do convex and concave lenses form images?"
</div>

**Key Theory Highlights:**
* Mirror/Lens formula: $\\frac{1}{f} = \\frac{1}{v} \\pm \\frac{1}{u}$.
* Snell's Law: $n_1 \\sin i = n_2 \\sin r$.

---
### 🔬 Interactive Bending Light & Optics Lab
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_en.html"></iframe>
</div>
"""

    # --- CHEMISTRY 1: Electrochemistry ---
    elif any(k in text for k in ["electrochemistry", "galvanic", "cell", "electrode potential"]):
        return """
### 🔋 Electrochemistry — Galvanic Cells, Voltage

<div class="suggestion-box">
<strong>💡 Aap aise questions puch sakte hain:</strong><br>
• "Explain the working of a Daniell Cell (Galvanic Cell)."<br>
• "What is Nernst Equation for electrode potential?"
</div>

**Key Theory Highlights:**
* Oxidation occurs at Anode (negative electrode), Reduction occurs at Cathode (positive electrode).
* Cell potential: $E_{cell} = E_{cathode} - E_{anode}$.

---
### 🔬 Interactive Electrochemical Cell Lab
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/battery-voltage/latest/battery-voltage_en.html"></iframe>
</div>
"""

    # --- CHEMISTRY 2: Chemical Kinetics ---
    elif any(k in text for k in ["kinetics", "reaction rate", "concentration", "order of reaction"]):
        return """
### ⏱️ Chemical Kinetics — Reaction Rate & Concentration

<div class="suggestion-box">
<strong>💡 Aap aise questions puch sakte hain:</strong><br>
• "What factors affect the rate of a chemical reaction?"<br>
• "What is the difference between molecularity and order of a reaction?"
</div>

**Key Theory Highlights:**
* Rate Law: Rate = $k[A]^x[B]^y$.
* Arrhenius Equation: $k = A e^{-E_a / RT}$.

---
### 🔬 Interactive Reaction Kinetics Lab
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/reactants-products-and-leftovers/latest/reactants-products-and-leftovers_en.html"></iframe>
</div>
"""

    # --- CHEMISTRY 3: Solutions ---
    elif any(k in text for k in ["solution", "molarity", "dilution", "colligative"]):
        return """
### 🧪 Solutions — Concentration, Molarity, Dilution

<div class="suggestion-box">
<strong>💡 Aap aise questions puch sakte hain:</strong><br>
• "What is the formula for calculating Molarity and Molality?"<br>
• "How does adding solute change solution concentration?"
</div>

**Key Theory Highlights:**
* **Molarity ($M$):** Moles of solute per liter of solution.
* **Raoult's Law:** Partial vapor pressure of each volatile component is directly proportional to its mole fraction.

---
### 🔬 Interactive Solution Concentration Lab
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/concentration/latest/concentration_en.html"></iframe>
</div>
"""

    # --- CHEMISTRY 4: Acids & Bases ---
    elif any(k in text for k in ["ph", "acid", "base", "indicator"]):
        return """
### ⚗️ Acids & Bases — pH and Indicators

<div class="suggestion-box">
<strong>💡 Aap aise questions puch sakte hain:</strong><br>
• "How to calculate the pH of a strong acid or base solution?"<br>
• "What are acid-base indicators?"
</div>

**Key Theory Highlights:**
* $\\text{pH} = -\\log[H^+]$.
* Neutral: $\\text{pH} = 7$, Acidic: $\\text{pH} < 7$, Basic: $\\text{pH} > 7$.

---
### 🔬 Interactive pH Scale Lab
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/ph-scale/latest/ph-scale_en.html?screens=1"></iframe>
</div>
"""

    # --- CHEMISTRY 5: Surface Chemistry ---
    elif any(k in text for k in ["surface chemistry", "adsorption", "colloid", "catalysis"]):
        return """
### 🧽 Surface Chemistry — Adsorption/Colloids

<div class="suggestion-box">
<strong>💡 Aap aise questions puch sakte hain:</strong><br>
• "What is the difference between physisorption and chemisorption?"<br>
• "What are lyophilic and lyophobic colloids?"
</div>

**Key Theory Highlights:**
* Freundlich Adsorption Isotherm: $\\frac{x}{m} = k P^{1/n}$ (at constant temperature).
* Tyndall effect is exhibited by colloidal solutions.

---
### 🔬 Interactive States of Matter & Surface Interaction
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/states-of-matter-basics/latest/states-of-matter-basics_en.html"></iframe>
</div>
"""

    # --- MATHS 1: Application of Derivatives ---
    elif any(k in text for k in ["derivative", "application of derivatives", "tangent", "maxima", "minima"]):
        return """
### 📈 Application of Derivatives (Class 12 Math)

<div class="suggestion-box">
<strong>💡 Aap aise questions puch sakte hain:</strong><br>
• "How to find the equation of tangent and normal to a curve?"<br>
• "What is the test for local maxima and local minima?"
</div>

**Key Theory Highlights:**
* Rate of change: $\\frac{dy}{dx}$ represents rate of change of $y$ with respect to $x$.
* Increasing function: $\\frac{dy}{dx} > 0$ | Decreasing function: $\\frac{dy}{dx} < 0$.

---
### 🔬 Interactive Function Visualizer
<div class="sim-container">
    <iframe src="https://www.geogebra.org/calculator?embed"></iframe>
</div>
"""

    # --- MATHS 2: Probability ---
    elif any(k in text for k in ["probability", "bayes", "conditional probability", "random variable"]):
        return """
### 🎲 Probability (Class 12 Math)

<div class="suggestion-box">
<strong>💡 Aap aise questions puch sakte hain:</strong><br>
• "What is conditional probability formula?"<br>
• "Explain Bayes' Theorem with an example."
</div>

**Key Theory Highlights:**
* Conditional Probability: $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$.
* Multiplication theorem: $P(A \\cap B) = P(A)P(B|A)$.

---
### 🔬 Interactive Probability Visualizer
<div class="sim-container">
    <iframe src="https://www.geogebra.org/calculator?embed"></iframe>
</div>
"""

    # --- FALLBACK / GENERAL QUERY ---
    else:
        return f"""
### 📘 ChitraVidya AI | Class 12 PCM Guide: **{query.title()}**

<div class="suggestion-box">
<strong>💡 Top topics available to explore:</strong><br>
• <strong>Physics:</strong> Electrostatics, Circuits, Magnetism, EMI, Ray Optics<br>
• <strong>Chemistry:</strong> Electrochemistry, Kinetics, Solutions, Acids & Bases, Surface Chemistry<br>
• <strong>Maths:</strong> Application of Derivatives, Probability
</div>

Aap upar diye gaye kisi bhi topic ka naam ya usse related question direct yahan type kar sakte hain!
"""

# 4. App Main Interface Logic (Header / Logo)
if len(st.session_state.messages) == 0:
    st.markdown("""
        <div class="title-container">
            <img src="https://img.icons8.com/color/96/sparkling.png" class="logo-img">
            <h1 class="main-title">Ask ChitraVidya AI</h1>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('<p class="sub-title">for Class 12th PCM</p>', unsafe_allow_html=True)

# Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

# 5. Bottom Chat Input & Auto-Scroll Mechanism
user_input = st.chat_input("Ask ChitraVidya AI...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate structured PCM response
    response = get_pcm_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Auto-scroll script injection for instant view focus
    st.markdown(
        """
        <script>
            window.parent.document.querySelector('section.main').scrollTo({top: 100000, behavior: 'smooth'});
        </script>
        """,
        unsafe_allow_html=True
    )
    
    st.rerun()
