import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Physics | Class 12", page_icon="⚡", layout="wide")
st.title("⚡ Class 12 Physics – Interactive Simulations")
st.caption("CBSE aligned • Free simulations • Source always shown")

def show_sim(title, desc, url, source="PhET Interactive Simulations (University of Colorado)", height=620):
    with st.expander(f"**{title}**", expanded=False):
        st.markdown(f"**Source:** `{source}`")
        st.write(desc)
        st.markdown(f"[Open full screen ↗]({url})")
        components.iframe(url, height=height, scrolling=True)

# ---------------- Electrostatics & Current ----------------
st.header("Unit I & II → Electrostatics + Current Electricity")

show_sim(
    "Charges and Fields",
    "Electric field, equipotential lines, force on charges. Perfect for Electric Charges & Fields + Electrostatic Potential.",
    "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html"
)

show_sim(
    "Capacitor Lab: Basics",
    "Change plate area, separation and voltage. See charge, energy stored and electric field. Direct match for Capacitance.",
    "https://phet.colorado.edu/sims/html/capacitor-lab-basics/latest/capacitor-lab-basics_en.html"
)

show_sim(
    "Circuit Construction Kit: DC",
    "Build real circuits with battery, resistors, bulbs, switches. Use voltmeter & ammeter. Best for Current Electricity.",
    "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html"
)

show_sim(
    "Ohm's Law",
    "Visualise V = IR relationship interactively.",
    "https://phet.colorado.edu/sims/html/ohms-law/latest/ohms-law_en.html"
)

# ---------------- Magnetism & EMI ----------------
st.header("Unit III & IV → Magnetism + Electromagnetic Induction & AC")

show_sim(
    "Faraday's Law",
    "Move a bar magnet through a coil and watch induced current. Classic EMI demonstration.",
    "https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html"
)

show_sim(
    "Faraday's Electromagnetic Lab",
    "Advanced lab – generator, transformer, electromagnet, pickup coil etc.",
    "https://phet.colorado.edu/sims/html/faradays-electromagnetic-lab/latest/faradays-electromagnetic-lab_en.html"
)

show_sim(
    "Generator",
    "See conversion of mechanical energy into electrical energy.",
    "https://phet.colorado.edu/sims/html/generator/latest/generator_en.html"
)

# ---------------- Optics ----------------
st.header("Unit VI → Optics")

show_sim(
    "Bending Light",
    "Snell’s law, reflection, refraction, total internal reflection and prisms.",
    "https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_en.html"
)

show_sim(
    "Geometric Optics",
    "Ray diagrams for lenses and mirrors, image formation, magnification.",
    "https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_en.html"
)

# ---------------- Dual Nature, Atoms, Nuclei ----------------
st.header("Unit VII – IX → Dual Nature, Atoms & Nuclei, Semiconductors")

show_sim(
    "Photoelectric Effect",
    "Intensity, frequency, stopping potential, work function – the classic experiment.",
    "https://phet.colorado.edu/sims/html/photoelectric-effect/latest/photoelectric-effect_en.html"
)

show_sim(
    "Build an Atom",
    "Add protons, neutrons and electrons. Make ions and isotopes.",
    "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_en.html"
)

show_sim(
    "Alpha Decay",
    "Watch radioactive decay and understand half-life visually.",
    "https://phet.colorado.edu/sims/html/alpha-decay/latest/alpha-decay_en.html"
)

st.success("All simulations above are free and officially from PhET.")
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Physics | Class 12", page_icon="⚡", layout="wide")
st.title("⚡ Class 12 Physics – Interactive Simulations")
st.caption("CBSE aligned • Free simulations • Source always shown")

def show_sim(title, desc, url, source="PhET Interactive Simulations (University of Colorado)", height=620):
    with st.expander(f"**{title}**", expanded=False):
        st.markdown(f"**Source:** `{source}`")
        st.write(desc)
        st.markdown(f"[Open full screen ↗]({url})")
        components.iframe(url, height=height, scrolling=True)

# ---------------- Electrostatics & Current ----------------
st.header("Unit I & II → Electrostatics + Current Electricity")

show_sim(
    "Charges and Fields",
    "Electric field, equipotential lines, force on charges. Perfect for Electric Charges & Fields + Electrostatic Potential.",
    "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html"
)

show_sim(
    "Capacitor Lab: Basics",
    "Change plate area, separation and voltage. See charge, energy stored and electric field. Direct match for Capacitance.",
    "https://phet.colorado.edu/sims/html/capacitor-lab-basics/latest/capacitor-lab-basics_en.html"
)

show_sim(
    "Circuit Construction Kit: DC",
    "Build real circuits with battery, resistors, bulbs, switches. Use voltmeter & ammeter. Best for Current Electricity.",
    "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html"
)

show_sim(
    "Ohm's Law",
    "Visualise V = IR relationship interactively.",
    "https://phet.colorado.edu/sims/html/ohms-law/latest/ohms-law_en.html"
)

# ---------------- Magnetism & EMI ----------------
st.header("Unit III & IV → Magnetism + Electromagnetic Induction & AC")

show_sim(
    "Faraday's Law",
    "Move a bar magnet through a coil and watch induced current. Classic EMI demonstration.",
    "https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html"
)

show_sim(
    "Faraday's Electromagnetic Lab",
    "Advanced lab – generator, transformer, electromagnet, pickup coil etc.",
    "https://phet.colorado.edu/sims/html/faradays-electromagnetic-lab/latest/faradays-electromagnetic-lab_en.html"
)

show_sim(
    "Generator",
    "See conversion of mechanical energy into electrical energy.",
    "https://phet.colorado.edu/sims/html/generator/latest/generator_en.html"
)

# ---------------- Optics ----------------
st.header("Unit VI → Optics")

show_sim(
    "Bending Light",
    "Snell’s law, reflection, refraction, total internal reflection and prisms.",
    "https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_en.html"
)

show_sim(
    "Geometric Optics",
    "Ray diagrams for lenses and mirrors, image formation, magnification.",
    "https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_en.html"
)

# ---------------- Dual Nature, Atoms, Nuclei ----------------
st.header("Unit VII – IX → Dual Nature, Atoms & Nuclei, Semiconductors")

show_sim(
    "Photoelectric Effect",
    "Intensity, frequency, stopping potential, work function – the classic experiment.",
    "https://phet.colorado.edu/sims/html/photoelectric-effect/latest/photoelectric-effect_en.html"
)

show_sim(
    "Build an Atom",
    "Add protons, neutrons and electrons. Make ions and isotopes.",
    "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_en.html"
)

show_sim(
    "Alpha Decay",
    "Watch radioactive decay and understand half-life visually.",
    "https://phet.colorado.edu/sims/html/alpha-decay/latest/alpha-decay_en.html"
)

st.success("All simulations above are free and officially from PhET.")
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Chemistry | Class 12", page_icon="🧪", layout="wide")
st.title("🧪 Class 12 Chemistry – Interactive Simulations")
st.caption("CBSE aligned • Free simulations • Source always shown")

def show_sim(title, desc, url, source="PhET Interactive Simulations", height=620):
    with st.expander(f"**{title}**", expanded=False):
        st.markdown(f"**Source:** `{source}`")
        st.write(desc)
        st.markdown(f"[Open full screen ↗]({url})")
        components.iframe(url, height=height, scrolling=True)

st.header("Physical Chemistry")

show_sim(
    "Concentration",
    "Change amount of solute and volume of solution. See molarity change in real time.",
    "https://phet.colorado.edu/sims/html/concentration/latest/concentration_en.html"
)

show_sim(
    "Acid-Base Solutions",
    "Explore strong/weak acids and bases, pH, and particle view.",
    "https://phet.colorado.edu/sims/html/acid-base-solutions/latest/acid-base-solutions_en.html"
)

show_sim(
    "Gas Properties",
    "Ideal gas law – change pressure, volume, temperature and number of particles.",
    "https://phet.colorado.edu/sims/html/gas-properties/latest/gas-properties_en.html"
)

show_sim(
    "States of Matter",
    "Solid, liquid, gas – heat/cool particles and observe phase changes.",
    "https://phet.colorado.edu/sims/html/states-of-matter/latest/states-of-matter_en.html"
)

st.header("Atomic Structure & Molecules")

show_sim(
    "Build a Molecule",
    "Start from atoms and build molecules. Great for understanding molecular formulas.",
    "https://phet.colorado.edu/sims/html/build-a-molecule/latest/build-a-molecule_en.html"
)

show_sim(
    "Molecule Shapes",
    "VSEPR theory – see 3D shapes of molecules based on electron pairs.",
    "https://phet.colorado.edu/sims/html/molecule-shapes/latest/molecule-shapes_en.html"
)

show_sim(
    "Build an Atom",
    "Protons, neutrons, electrons → ions and isotopes.",
    "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_en.html"
)

st.success("All simulations are free from PhET.")
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mathematics | Class 12", page_icon="📐", layout="wide")
st.title("📐 Class 12 Mathematics – Interactive Simulations")
st.caption("CBSE aligned • Free tools • Source always shown")

def show_sim(title, desc, url, source="PhET Interactive Simulations", height=620):
    with st.expander(f"**{title}**", expanded=False):
        st.markdown(f"**Source:** `{source}`")
        st.write(desc)
        st.markdown(f"[Open full screen ↗]({url})")
        components.iframe(url, height=height, scrolling=True)

st.header("Functions, Graphs & Calculus")

show_sim(
    "Graphing Lines",
    "Slope-intercept form, point-slope form – explore linear equations visually.",
    "https://phet.colorado.edu/sims/html/graphing-lines/latest/graphing-lines_en.html"
)

show_sim(
    "Graphing Quadratics",
    "See how coefficients a, b, c affect the parabola.",
    "https://phet.colorado.edu/sims/html/graphing-quadratics/latest/graphing-quadratics_en.html"
)

show_sim(
    "Calculus Grapher",
    "Visualise derivatives and integrals interactively.",
    "https://phet.colorado.edu/sims/html/calculus-grapher/latest/calculus-grapher_en.html"
)

st.header("Vectors & 3D Geometry")

show_sim(
    "Vector Addition",
    "Add vectors graphically and see resultant.",
    "https://phet.colorado.edu/sims/html/vector-addition/latest/vector-addition_en.html"
)

st.info("For advanced 3D geometry and matrices you can also use free tools like GeoGebra (geogebra.org) and Desmos (desmos.com).")
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Biology | Class 12", page_icon="🧬", layout="wide")
st.title("🧬 Class 12 Biology – Interactive Simulations")
st.caption("CBSE aligned • Free simulations • Source always shown")

def show_sim(title, desc, url, source, height=620):
    with st.expander(f"**{title}**", expanded=False):
        st.markdown(f"**Source:** `{source}`")
        st.write(desc)
        st.markdown(f"[Open full screen ↗]({url})")
        components.iframe(url, height=height, scrolling=True)

st.header("Genetics & Evolution")

show_sim(
    "Gene Expression Essentials",
    "Transcription and translation – see how DNA becomes protein.",
    "https://phet.colorado.edu/sims/html/gene-expression-essentials/latest/gene-expression-essentials_en.html",
    "PhET Interactive Simulations"
)

show_sim(
    "Natural Selection",
    "Watch evolution happen through natural selection in a population.",
    "https://phet.colorado.edu/sims/html/natural-selection/latest/natural-selection_en.html",
    "PhET Interactive Simulations"
)

st.header("Other Useful Free Tools")

st.markdown("""
- **Classical Genetics Simulator** (Fruit fly crosses) → [cgslab.com](https://cgslab.com)  
  **Source:** Classical Genetics Simulator
- **HHMI BioInteractive** (excellent free interactives) → [biointeractive.org](https://www.biointeractive.org)
""")

st.success("PhET simulations + other free high-quality biology tools.")
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="IP | Class 12", page_icon="💻", layout="wide")
st.title("💻 Class 12 Informatics Practices")
st.caption("Live demos + free tools • Source always shown")

st.header("1. Data Handling using Pandas (Live Demo)")

# Sample data
data = {
    "Name": ["Aman", "Riya", "Kabir", "Sneha", "Vikram"],
    "Marks": [85, 92, 78, 88, 95],
    "City": ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai"]
}
df = pd.DataFrame(data)

st.write("Sample DataFrame:")
st.dataframe(df, use_container_width=True)

st.write("Basic operations:")
col1, col2 = st.columns(2)
with col1:
    st.write("Head of data:")
    st.write(df.head(3))
with col2:
    st.write("Describe:")
    st.write(df.describe())

st.header("2. Data Visualization (Matplotlib)")

fig, ax = plt.subplots()
ax.bar(df["Name"], df["Marks"], color="#3b82f6")
ax.set_ylabel("Marks")
ax.set_title("Student Marks")
st.pyplot(fig)

st.header("3. Useful Free Tools for IP")

st.markdown("""
| Topic | Free Tool | Source |
|-------|-----------|--------|
| SQL Practice | [SQLBolt](https://sqlbolt.com) / [DB Fiddle](https://www.db-fiddle.com) | SQLBolt / DB Fiddle |
| Pandas Practice | This page itself + [Kaggle](https://www.kaggle.com) | Live demo |
| Computer Networks | [Cisco Packet Tracer](https://www.netacad.com) (free student version) | Cisco |
| Societal Impacts | Read CBSE textbook + [Internet Society](https://www.internetsociety.org) resources | Open resources |
""")

st.success("All tools recommended above are free for students.")
