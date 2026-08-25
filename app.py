import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="ChitraVidya AI | Class 12 PCM",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Minimal Clean UI (ChatGPT Style Center Title with Logo)
st.markdown("""
    <style>
    .title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        margin-top: 10vh;
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
    </style>
""", unsafe_allow_html=True)

# 2. State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Dynamic PCM Router & Content Engine
def get_pcm_response(query):
    text = query.lower()
    
    # --- A. PHYSICS ---
    if any(k in text for k in ["solenoid", "magnetic field due to current", "biot savart", "ampere"]):
        return """
### ⚡ Magnetic Effects of Current & Solenoid

**Key Theory Highlights:**
* **Solenoid:** A tightly wound helical coil of insulated copper wire.
* **Magnetic Field inside:** Uniform and parallel along the axis ($B = \mu_0 n I$).
* **Outside Field:** Nearly zero for an ideal long solenoid.

---
### 🔬 Interactive Electromagnetic Field Simulator
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_all.html"></iframe>
</div>

---
**💡 How to Use This Simulation (Beginner Guide):**
1. **Magnet Move Karein:** Bar magnet ko drag karke coil ke andar-baahar move karein.
2. **Observe Bulb & Voltmeter:** Observe karein ki jab magnet move hota hai tabhi bulb glow karta hai (Induction).
3. **Lines View:** "Show Magnetic Field Lines" checkbox par click karke magnetic lines dekhein.
"""

    elif any(k in text for k in ["induction", "faraday", "lenz", "emi"]):
        return """
### 🧲 Electromagnetic Induction (EMI)

**Key Theory Highlights:**
* **Faraday's Law:** Induced EMF is directly proportional to the rate of change of magnetic flux ($\mathcal{E} = -\\frac{d\Phi}{dt}$).
* **Lenz's Law:** Induced current opposes the change in flux that produces it (Conservation of Energy).

---
### 🔬 Interactive EMI Simulator
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_all.html"></iframe>
</div>

---
**💡 How to Use This Simulation (Beginner Guide):**
1. Magnet ki speed badha kar dekhein: Fast movement se zyada current generate hota hai.
2. Magnet ke poles (N/S) ko flip karke voltmeter ki direction change hote hue dekhein.
"""

    elif any(k in text for k in ["circuit", "ohm", "resistance", "current electricity", "kirchhoff"]):
        return """
### 🔌 Current Electricity & Circuit Construction

**Key Theory Highlights:**
* **Ohm's Law:** $V = IR$ (at constant temperature).
* **Kirchhoff's Voltage Law (KVL):** $\sum V = 0$ in a closed loop.
* **Kirchhoff's Current Law (KCL):** $\sum I_{in} = \sum I_{out}$ at any junction.

---
### 🔬 Interactive Circuit Construction Kit
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_all.html"></iframe>
</div>

---
**💡 How to Use This Simulation (Beginner Guide):**
1. **Components Drag Karein:** Wire, Battery, aur Resistor/Bulb ko screen par laayein.
2. **Circuit Close Karein:** Wires ko connect karke complete loop banayein.
3. **Voltmeter & Ammeter:** Side panel se Voltmeter drag karke $V$ aur $I$ measure karein.
"""

    elif any(k in text for k in ["wave optics", "interference", "diffraction", "huygen", "young"]):
        return """
### 🌊 Wave Optics & Wave Interference

**Key Theory Highlights:**
* **Huygens' Principle:** Every point on a wavefront acts as a secondary source of spherical wavelets.
* **Young's Double Slit (YDSE):** Fringe width $\beta = \\frac{\lambda D}{d}$.

---
### 🔬 Interactive Wave Interference Simulator
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/wave-interference/latest/wave-interference_all.html"></iframe>
</div>

---
**💡 How to Use This Simulation (Beginner Guide):**
1. Screen par "Slits" option select karein.
2. Light generator ON karein aur Slit width adjust karke screen par alternate bright/dark fringes dekhein.
"""

    # --- B. CHEMISTRY ---
    elif any(k in text for k in ["vsepr", "molecule shape", "molecular geometry", "chemical bonding"]):
        return """
### 💎 Molecular Geometry & VSEPR Theory

**Key Theory Highlights:**
* Electron pairs around a central atom repel each other and adjust in 3D space to minimize repulsion.
* **Linear:** $180^\circ$ | **Tetrahedral:** $109.5^\circ$ | **Trigonal Planar:** $120^\circ$

---
### 🔬 Interactive 3D Molecule Visualizer
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/molecule-shapes/latest/molecule-shapes_all.html"></iframe>
</div>

---
**💡 How to Use This Simulation (Beginner Guide):**
1. Screen par **Real Molecules** select karein.
2. Central atom ke surrounding bonded atoms aur lone pairs add/remove karke 3D shape rotate karein.
3. **Show Bond Angles** checkmark on karke exact angle observe karein.
"""

    elif any(k in text for k in ["ph", "acid", "base", "solution", "electrochemistry"]):
        return """
### 🧪 Acids, Bases & pH Scale

**Key Theory Highlights:**
* **pH Definition:** $\text{pH} = -\log[H^+]$.
* Neutral: $\text{pH} = 7$, Acidic: $\text{pH} < 7$, Basic: $\text{pH} > 7$.

---
### 🔬 Interactive pH Scale Simulator
<div class="sim-container">
    <iframe src="https://phet.colorado.edu/sims/html/ph-scale/latest/ph-scale_all.html"></iframe>
</div>

---
**💡 How to Use This Simulation (Beginner Guide):**
1. Dropper se liquid container mein dalein.
2. Green pH sensor ko liquid mein dip karke exact pH level check karein.
3. Water add karke dilution effect test karein.
"""

    # --- C. MATHEMATICS ---
    elif any(k in text for k in ["3d", "vector", "plane", "line", "skew", "geometry", "math"]):
        return """
### 📐 3D Geometry & Vectors (Class 12)

**Key Theory Highlights:**
* **Vector Product:** $\vec{A} \times \vec{B} = |A||B|\sin\theta\,\hat{n}$.
* **Shortest Distance (Skew Lines):** $d = \left| \\frac{(\vec{b}_1 \times \vec{b}_2) \cdot (\vec{a}_2 - \vec{a}_1)}{|\vec{b}_1 \times \vec{b}_2|} \right|$.

---
### 🔬 Interactive 3D Math Canvas (GeoGebra 3D)
<div class="sim-container">
    <iframe src="https://www.geogebra.org/3d?embed"></iframe>
</div>

---
**💡 How to Use This Canvas (Beginner Guide):**
* **Cube Render:** Left side **Algebra ($\alpha$)** tab mein `Cube((0,0,0), (2,0,0))` type karke Enter dabayein.
* **Vector Render:** Algebra tab mein `Vector((2,3,4))` type karein.
* **Rotate Canvas:** Mouse click karke Hold & Drag karne par 3D space rotate hoga.
"""

    # --- FALLBACK / GENERAL QUERY RESPONSE ---
    else:
        return f"""
### 📘 CBSE Class 12 PCM Topic: **{query.title()}**

**Concept Overview:**
Class 12th CBSE 2026-27 syllabus ke according **{query.title()}** ek core concept hai. Aap isse related specific simulations screen par dekhne ke liye neechay diye gaye keywords me se search kar sakte hain.

**Try searching:**
* **Physics:** *Solenoid, Electromagnetic Induction, Kirchhoff Laws, Wave Optics*
* **Chemistry:** *VSEPR Theory, Molecule Shapes, pH Scale*
* **Mathematics:** *3D Geometry, Vectors*
"""

# 4. App Main Interface Logic (Only show when chat is empty)
if len(st.session_state.messages) == 0:
    st.markdown("""
        <div class="title-container">
            <img src="https://raw.githubusercontent.com/chitravidya-ai/chitravidya-ai/main/logo.png" class="logo-img">
            <h1 class="main-title" style="margin:0;">Ask ChitraVidya AI</h1>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('<p class="sub-title">for Class 12th</p>', unsafe_allow_html=True)

# Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

# 5. Bottom Chat Input
user_input = st.chat_input("Ask ChitraVidya AI...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate structured PCM response
    response = get_pcm_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()
