import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Class 12 CBSE Learning Hub",
    page_icon="📚",
    layout="wide",
)

TOPICS = {
    # ==================== PHYSICS THEORY ====================
    "Electric Charges and Fields": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "Electric charge is a fundamental property of matter. Like charges repel; unlike charges attract.",
            "Coulomb's law: F = k|q₁q₂|/r², where k = 1/(4πε₀) ≈ 9 × 10⁹ N m²/C² in vacuum.",
            "Electric field magnitude due to a point charge: E = k|q|/r². It points away from a positive charge and toward a negative charge.",
            "Electric field lines never intersect. Their density indicates relative field strength.",
            "Gauss's law: ∮ E·dA = Q_enclosed/ε₀."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html",
        "beginner": [
            "Place positive and negative charges and compare field patterns.",
            "Display equipotential lines and compare them with electric field lines.",
            "Move a test charge and observe the electric force."
        ],
    },
    "Electrostatic Potential and Capacitance": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "Electric potential is potential energy per unit charge. For a point charge, V = kq/r.",
            "Potential difference is the change in electric potential between two points.",
            "Capacitance: C = Q/V. For an ideal parallel-plate capacitor in vacuum, C = ε₀A/d.",
            "Energy stored in a capacitor: U = ½CV² = Q²/(2C) = ½QV.",
            "A dielectric changes capacitance; charge and energy changes depend on whether the capacitor remains connected to a battery."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/capacitor-lab-basics/latest/capacitor-lab-basics_en.html",
        "beginner": [
            "Change plate area and separation and observe capacitance.",
            "Add a dielectric and observe the changes."
        ],
    },
    "Current Electricity": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "Ohm's law: V = IR for an ohmic conductor under constant physical conditions.",
            "Resistance of a uniform wire: R = ρL/A.",
            "Kirchhoff's junction rule expresses conservation of charge; the loop rule expresses conservation of energy.",
            "A Wheatstone bridge is balanced when the resistance ratios of the two pairs of arms are equal, according to the circuit labelling.",
            "Emf is energy supplied per unit charge. For an ideal open-circuit measurement, terminal voltage equals emf."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html",
        "beginner": [
            "Build series and parallel circuits.",
            "Use ammeters and voltmeters to measure current and voltage.",
            "Change resistance and voltage to test V = IR."
        ],
    },
    "Moving Charges and Magnetism": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "Magnetic force on a moving charge: F = q(v × B); magnitude = |q|vB sin θ.",
            "Force on a current-carrying wire: F = I(L × B); magnitude = BIL sin θ.",
            "The Biot–Savart law describes the magnetic field contribution from a current element.",
            "Ampère's circuital law relates the closed line integral of the magnetic field to enclosed current.",
            "A moving-coil galvanometer works because a current-carrying coil experiences torque in a magnetic field."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/magnets-and-electromagnets/latest/magnets-and-electromagnets_en.html",
        "beginner": [
            "Observe the field around a bar magnet and an electromagnet.",
            "Change coil current or turns where supported."
        ],
    },
    "Magnetism and Matter": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "Magnetic field lines form closed loops; outside a bar magnet they run from north to south.",
            "Materials can be classified as diamagnetic, paramagnetic or ferromagnetic.",
            "A bar magnet can be modelled as a magnetic dipole.",
            "Earth's magnetic field is described using declination, inclination and horizontal component.",
            "Magnetic susceptibility and permeability describe how a material responds to an applied magnetic field."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/magnets-and-electromagnets/latest/magnets-and-electromagnets_en.html",
        "beginner": [
            "Inspect the field-line pattern around a bar magnet.",
            "Compare a permanent magnet with an electromagnet."
        ],
    },
    "Electromagnetic Induction": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "Faraday's law: ε = −d(NΦ)/dt, where NΦ is magnetic flux linkage.",
            "Lenz's law states that induced current opposes the change in magnetic flux that produces it.",
            "For a linear inductor, NΦ = LI. Energy stored: U = ½LI².",
            "Mutual induction occurs when changing current in one circuit changes magnetic flux through another circuit.",
            "Eddy currents are circulating currents induced in bulk conductors. Laminating a core can reduce them."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html",
        "beginner": [
            "Move a magnet into and out of a coil.",
            "Compare the induced response when the magnet moves slowly and quickly."
        ],
    },
    "Alternating Current": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "Sinusoidal alternating voltage: v(t) = V₀ sin(ωt).",
            "In a pure resistor, current and voltage are in phase.",
            "In an ideal inductor, current lags voltage by 90°; in an ideal capacitor, current leads voltage by 90°.",
            "At series LCR resonance, X_L = X_C and impedance is purely resistive.",
            "Average power for sinusoidal AC: P = V_rms I_rms cos φ."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/circuit-construction-kit-ac/latest/circuit-construction-kit-ac_en.html",
        "beginner": [
            "Build an AC circuit and observe current and voltage behaviour.",
            "Explore the effect of circuit components where supported."
        ],
    },
    "Electromagnetic Waves": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "Electromagnetic waves are transverse waves consisting of oscillating electric and magnetic fields.",
            "In vacuum, their speed is c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s.",
            "The electric field, magnetic field and direction of propagation are mutually perpendicular in a plane wave.",
            "The electromagnetic spectrum includes radio waves, microwaves, infrared, visible light, ultraviolet, X-rays and gamma rays.",
            "All electromagnetic waves travel at the same speed in vacuum but differ in frequency and wavelength."
        ],
        "simulation": None,
        "beginner": [],
    },
    "Ray Optics and Optical Instruments": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "Using the Cartesian sign convention, thin-lens formula: 1/f = 1/v − 1/u.",
            "For spherical mirrors under the Cartesian sign convention: 1/f = 1/v + 1/u.",
            "For a thin lens, magnification m = hᵢ/hₒ = v/u.",
            "Total internal reflection requires light to travel from an optically denser to a rarer medium and the incidence angle to exceed the critical angle.",
            "Microscopes and telescopes use combinations of optical elements to produce magnified images."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_en.html",
        "beginner": [
            "Change object distance and observe image position and orientation.",
            "Compare convex and concave lenses."
        ],
    },
    "Wave Optics": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "Huygens' principle describes each point on a wavefront as a source of secondary wavelets.",
            "Young's double-slit experiment demonstrates interference and the wave nature of light.",
            "For small angles, fringe width β = λD/d.",
            "Diffraction is the spreading of waves around an aperture or obstacle.",
            "Polarisation demonstrates the transverse nature of light waves."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/wave-interference/latest/wave-interference_en.html",
        "beginner": [
            "Explore constructive and destructive interference.",
            "Change wave settings and observe the pattern."
        ],
    },
    "Dual Nature of Radiation and Matter": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "The photoelectric effect is the emission of electrons when suitable electromagnetic radiation falls on a material.",
            "Einstein's photoelectric equation: hν = φ + K_max.",
            "For stopping potential V_s, maximum kinetic energy K_max = eV_s.",
            "The de Broglie wavelength is λ = h/p.",
            "Electron diffraction experiments provide evidence for the wave nature of matter."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/photoelectric-effect/latest/photoelectric-effect_en.html",
        "beginner": [
            "Change light frequency and intensity separately.",
            "Observe threshold frequency, stopping potential and photocurrent."
        ],
    },
    "Atoms": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "Rutherford's scattering experiment established the existence of a small, dense, positively charged nucleus.",
            "In the Bohr model of hydrogen, angular momentum is quantised: mvr = nℏ.",
            "Hydrogen energy levels: E_n = −13.6/n² eV.",
            "Hydrogen spectral series include Lyman, Balmer and Paschen.",
            "The Bohr model explains important features of hydrogen spectra but does not fully describe multi-electron atoms."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_en.html",
        "beginner": [
            "Add protons, neutrons and electrons to explore atomic composition.",
            "This simulation builds atoms; it is not a complete hydrogen spectral-line simulator."
        ],
    },
    "Nuclei": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "Mass defect is the difference between the sum of constituent nucleon masses and the measured nuclear mass.",
            "Binding energy is related to mass defect by E = Δmc².",
            "Radioactive decay is random for individual nuclei; large samples follow an exponential decay law.",
            "Half-life and decay constant are related by T₁/₂ = ln 2/λ ≈ 0.693/λ.",
            "Fission splits a heavy nucleus; fusion combines light nuclei. Both can release energy under suitable conditions."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/alpha-decay/latest/alpha-decay_en.html",
        "beginner": [
            "Observe the random nature of alpha decay.",
            "Compare individual decay with the behaviour of a large sample where supported."
        ],
    },
    "Semiconductor Electronics": {
        "subject": "Physics",
        "category": "Theory",
        "points": [
            "Intrinsic semiconductors are pure; doping produces extrinsic n-type or p-type semiconductors.",
            "A p–n junction diode conducts strongly under forward bias and has very small reverse current before breakdown.",
            "Rectifiers convert alternating current into pulsating direct current.",
            "A Zener diode can regulate voltage in its reverse-breakdown region when properly current-limited.",
            "Transistors can act as switches or amplifiers in suitable circuit configurations."
        ],
        "simulation": None,
        "beginner": [],
    },

    # ==================== PHYSICS PRACTICALS ====================
    "Meter Bridge": {
        "subject": "Physics Practical",
        "category": "Practical",
        "points": [
            "A meter bridge is based on the Wheatstone bridge principle.",
            "It determines an unknown resistance by balancing a bridge circuit.",
            "At balance, the resistance ratio in the gaps equals the ratio of corresponding wire-segment resistances; confirm the ratio order from your circuit diagram.",
            "For a uniform bridge wire, resistance is proportional to length when material and cross-section are constant.",
            "End effects, contact resistance and heating can affect measurements."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html",
        "beginner": [
            "Practise series circuits and resistance measurement.",
            "This is a conceptual aid, not a dedicated virtual meter bridge."
        ],
    },
    "Potentiometer": {
        "subject": "Physics Practical",
        "category": "Practical",
        "points": [
            "A potentiometer compares emf using potential drop along a uniform wire carrying steady current.",
            "For two cells measured under the same conditions, E₁/E₂ = l₁/l₂.",
            "If l₁ is the balance length for emf E and l₂ is the balance length for terminal voltage V through external resistance R, internal resistance r = R(l₁ − l₂)/l₂.",
            "At the null point, an ideal potentiometer draws no current from the cell being measured.",
            "Keep current stable and avoid heating the wire."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html",
        "beginner": [
            "Use a potential-divider circuit to visualise voltage drop.",
            "This is not a dedicated potentiometer experiment."
        ],
    },
    "Galvanometer Resistance and Conversion": {
        "subject": "Physics Practical",
        "category": "Practical",
        "points": [
            "A galvanometer detects small currents; its figure of merit is the current required per scale division.",
            "The half-deflection method can estimate galvanometer resistance under the assumptions of the lab procedure.",
            "A galvanometer is converted to an ammeter by connecting a low resistance shunt in parallel.",
            "It is converted to a voltmeter by connecting a high resistance in series.",
            "Follow the exact circuit and calculation method in your school practical manual."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html",
        "beginner": [
            "Explore how series and parallel resistance change current.",
            "The simulation may not provide a dedicated galvanometer setup."
        ],
    },
    "Focal Length of a Convex Lens": {
        "subject": "Physics Practical",
        "category": "Practical",
        "points": [
            "The focal length of a convex lens can be estimated using the object-distance and image-distance method.",
            "With the Cartesian sign convention, the thin-lens equation is 1/f = 1/v − 1/u.",
            "Measure object and real-image positions carefully and apply the sign convention consistently.",
            "Repeat measurements at several positions and calculate an average focal length.",
            "The lens-maker equation relates focal length to refractive index and surface curvatures for a thin lens in air."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_en.html",
        "beginner": [
            "Change object distance and observe image formation.",
            "Record object and image positions if the simulation permits meaningful measurements."
        ],
    },
    "Refractive Index of a Prism": {
        "subject": "Physics Practical",
        "category": "Practical",
        "points": [
            "At minimum deviation, refractive index of a prism in air is μ = sin[(A + D_min)/2] / sin(A/2).",
            "A is the prism angle and D_min is the angle of minimum deviation.",
            "At minimum deviation, the ray path is symmetric and angle of incidence equals angle of emergence.",
            "Take angular readings carefully and repeat observations to reduce random error.",
            "Dispersion occurs because refractive index generally depends on wavelength."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_en.html",
        "beginner": [
            "Explore refraction through different materials and angles.",
            "This may not reproduce a complete spectrometer procedure."
        ],
    },
    "Ohm's Law Verification": {
        "subject": "Physics Practical",
        "category": "Practical",
        "points": [
            "Ohm's law states V ∝ I when physical conditions, especially temperature, remain constant.",
            "The V–I graph is a straight line through the origin for an ideal ohmic conductor.",
            "The slope of a V-versus-I graph is resistance R; the slope of an I-versus-V graph is conductance.",
            "Take multiple readings and avoid heating the resistor significantly.",
            "Non-ohmic devices do not have a constant V/I ratio under all operating conditions."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/ohms-law/latest/ohms-law_en.html",
        "beginner": [
            "Change voltage and observe current.",
            "Check whether V/I remains approximately constant."
        ],
    },

    # ==================== CHEMISTRY THEORY ====================
    "Solutions": {
        "subject": "Chemistry",
        "category": "Theory",
        "points": [
            "Concentration may be expressed as molarity, molality, mole fraction and other measures.",
            "For an ideal solution, Raoult's law for a volatile component is pᵢ = xᵢpᵢ⁰.",
            "Colligative properties depend on the number of dissolved particles relative to solvent for sufficiently dilute solutions.",
            "Important colligative properties include relative lowering of vapour pressure, boiling-point elevation, freezing-point depression and osmotic pressure.",
            "The van't Hoff factor accounts for effective particle-number changes due to association or dissociation."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/concentration/latest/concentration_en.html",
        "beginner": [
            "Change solute amount and solution volume to observe concentration.",
            "This simulation does not demonstrate every colligative property."
        ],
    },
    "Electrochemistry": {
        "subject": "Chemistry",
        "category": "Theory",
        "points": [
            "A galvanic cell converts energy from a spontaneous redox reaction into electrical energy.",
            "Nernst equation: E = E° − (RT/nF) ln Q for the cell reaction as written.",
            "Standard electrode potentials are measured relative to the standard hydrogen electrode.",
            "Conductance is the reciprocal of resistance; conductivity and molar conductivity are different quantities.",
            "Kohlrausch's law describes limiting molar conductivity as the sum of ionic contributions."
        ],
        "simulation": None,
        "beginner": [],
    },
    "Chemical Kinetics": {
        "subject": "Chemistry",
        "category": "Theory",
        "points": [
            "Reaction rate can depend on concentration, temperature, catalysts and reaction mechanism.",
            "Reaction order is determined experimentally; molecularity applies to an elementary step.",
            "For a first-order reaction, ln([A]₀/[A]) = kt.",
            "For a first-order reaction, t₁/₂ = 0.693/k and is independent of initial concentration.",
            "Arrhenius equation: k = A exp(−Eₐ/RT)."
        ],
        "simulation": None,
        "beginner": [],
    },
    "The d- and f-Block Elements": {
        "subject": "Chemistry",
        "category": "Theory",
        "points": [
            "Transition elements commonly form ions with partially filled d subshells, though definitions and exceptions matter.",
            "Many transition-metal compounds show variable oxidation states, colour and catalytic behaviour.",
            "Lanthanoid contraction is the gradual decrease in lanthanoid ionic radii across the series.",
            "Actinoids are radioactive and commonly show a wider range of oxidation states than lanthanoids.",
            "Potassium permanganate and potassium dichromate are important oxidising agents in traditional Class 12 chemistry."
        ],
        "simulation": None,
        "beginner": [],
    },
    "Coordination Compounds": {
        "subject": "Chemistry",
        "category": "Theory",
        "points": [
            "Coordination compounds contain a central atom or ion bonded to surrounding ligands.",
            "Coordination number is the number of donor atoms directly bonded to the central metal.",
            "IUPAC naming depends on ligand names, ligand order, oxidation state and complex charge.",
            "Common isomerism types include geometrical, optical, linkage and ionisation isomerism.",
            "Valence Bond Theory and Crystal Field Theory offer different models for bonding and properties."
        ],
        "simulation": None,
        "beginner": [],
    },
    "Haloalkanes and Haloarenes": {
        "subject": "Chemistry",
        "category": "Theory",
        "points": [
            "Haloalkanes have a halogen attached to an aliphatic carbon; haloarenes have a halogen attached directly to an aromatic ring.",
            "Nucleophilic substitution in suitable haloalkanes can proceed by SN1 or SN2 mechanisms.",
            "Haloarenes are generally less reactive toward nucleophilic substitution than comparable haloalkanes because of the aryl C–X bond and resonance effects.",
            "Named reactions include Wurtz, Fittig and Sandmeyer reactions; conditions and substrates matter.",
            "Some polyhalogen compounds have important industrial or historical uses and significant environmental or health concerns."
        ],
        "simulation": None,
        "beginner": [],
    },
    "Alcohols, Phenols and Ethers": {
        "subject": "Chemistry",
        "category": "Theory",
        "points": [
            "Alcohols contain an –OH group bonded to a saturated carbon; phenols have –OH directly bonded to an aromatic ring.",
            "Phenols are generally more acidic than comparable aliphatic alcohols because the phenoxide ion is resonance-stabilised.",
            "Important alcohol reactions include oxidation, dehydration and esterification under suitable conditions.",
            "Phenols commonly undergo electrophilic aromatic substitution.",
            "Williamson ether synthesis prepares ethers using an alkoxide and a suitable primary alkyl halide."
        ],
        "simulation": None,
        "beginner": [],
    },
    "Aldehydes, Ketones and Carboxylic Acids": {
        "subject": "Chemistry",
        "category": "Theory",
        "points": [
            "Aldehydes and ketones contain the carbonyl group, C=O.",
            "Nucleophilic addition is characteristic of many aldehydes and ketones.",
            "Aldehydes are generally more readily oxidised than ketones and are often more reactive toward nucleophilic addition than comparable ketones.",
            "Carboxylic acids are acidic partly because their conjugate-base carboxylate ion is resonance-stabilised.",
            "Common tests include Tollens', Fehling's and 2,4-DNP tests; applicability depends on the compound."
        ],
        "simulation": None,
        "beginner": [],
    },
    "Amines": {
        "subject": "Chemistry",
        "category": "Theory",
        "points": [
            "Amines are derivatives of ammonia in which one or more hydrogen atoms are replaced by organic groups.",
            "The relative basicity of amines depends on solvent, structure, steric effects and solvation; simple order rules have exceptions.",
            "Amines can be prepared by several routes, including reduction of nitro compounds and suitable nitrile or amide reactions.",
            "The carbylamine test is characteristic of primary amines under prescribed conditions.",
            "Aromatic diazonium salts are useful intermediates in preparing substituted aromatic compounds."
        ],
        "simulation": None,
        "beginner": [],
    },
    "Biomolecules": {
        "subject": "Chemistry",
        "category": "Theory",
        "points": [
            "Carbohydrates include polyhydroxy aldehydes or ketones and compounds that yield them on hydrolysis.",
            "Proteins are polymers of amino acids joined by peptide bonds.",
            "Many enzymes are proteins that act as biological catalysts.",
            "DNA and RNA are nucleic acids involved in storing, transmitting or expressing genetic information.",
            "Vitamins are organic micronutrients required in small quantities for normal biological function."
        ],
        "simulation": None,
        "beginner": [],
    },

    # ==================== CHEMISTRY PRACTICALS ====================
    "Acid–Base Titration": {
        "subject": "Chemistry Practical",
        "category": "Practical",
        "points": [
            "Titration determines the amount or concentration of a solution using a solution of known concentration.",
            "Indicators such as phenolphthalein or methyl orange are chosen according to the equivalence-point region.",
            "The end point is the observed indicator change and should be close to the equivalence point.",
            "For a 1:1 acid–base reaction, MₐVₐ = MᵦVᵦ. For other stoichiometric ratios, use the balanced reaction.",
            "Use clean apparatus, read the burette at eye level and follow laboratory safety instructions."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/acid-base-solutions/latest/acid-base-solutions_en.html",
        "beginner": [
            "Explore how adding acid or base changes pH.",
            "This is a conceptual aid, not a full virtual burette titration."
        ],
    },
    "pH and Indicators": {
        "subject": "Chemistry Practical",
        "category": "Practical",
        "points": [
            "For dilute aqueous solutions, pH is often approximated as −log₁₀[H⁺]; the rigorous definition uses hydrogen-ion activity.",
            "Acid–base indicators change colour over characteristic pH transition ranges.",
            "Litmus, methyl orange and phenolphthalein are common indicators.",
            "Choose an indicator based on the equivalence-point region rather than using one indicator for every titration.",
            "Wear suitable protective equipment and never taste laboratory chemicals."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/acid-base-solutions/latest/acid-base-solutions_en.html",
        "beginner": [
            "Change acid or base concentration and observe pH.",
            "Explore indicator colour changes where supported."
        ],
    },
}


def render_topic(topic_name, topic):
    st.subheader(topic_name)
    st.caption(f"{topic['subject']} · {topic['category']}")

    st.markdown("#### Key Notes")
    for point in topic.get("points", []):
        st.markdown(f"- {point}")

    beginner = topic.get("beginner", [])
    if beginner:
        st.markdown("#### Try It")
        for step in beginner:
            st.markdown(f"- {step}")

    url = topic.get("simulation")
    if url:
        st.markdown("#### Learning Resource")
        st.markdown("**Source:** PhET Interactive Simulations, University of Colorado Boulder")
        st.markdown(f"[Open simulation in a new tab ↗]({url})")

        with st.expander("Open simulation inside this page", expanded=False):
            st.caption(
                "Some websites block embedding. If the simulation does not load, "
                "use the link above to open it in a new tab."
            )
            components.iframe(url, height=600, scrolling=True)
    else:
        st.info("No simulation is listed for this topic. Use your textbook and teacher-provided resources.")


st.title("📚 Class 12 CBSE Learning Hub")
st.caption("Physics and Chemistry • Revision Notes • Practicals • Free External Simulations")

st.warning(
    "Study aid only. Check the current official CBSE syllabus and your school's "
    "practical instructions. This app is not an official CBSE publication."
)

with st.sidebar:
    st.header("Find a Topic")

    subject_options = [
        "All",
        "Physics",
        "Physics Practical",
        "Chemistry",
        "Chemistry Practical",
    ]

    selected_subject = st.selectbox("Subject", subject_options)
    search_text = st.text_input("Search topic or keyword").strip().lower()
    show_sim_only = st.checkbox("Only topics with simulations", value=False)

    st.divider()
    st.markdown("### Useful Links")
    st.markdown("[CBSE Academic](https://cbseacademic.nic.in/)")
    st.markdown("[PhET Simulations](https://phet.colorado.edu/)")

filtered_topics = []

for name, topic in TOPICS.items():
    if selected_subject != "All" and topic["subject"] != selected_subject:
        continue

    if search_text:
        searchable_text = name.lower() + " " + " ".join(topic.get("points", [])).lower()
        if search_text not in searchable_text:
            continue

    if show_sim_only and not topic.get("simulation"):
        continue

    filtered_topics.append((name, topic))

col1, col2, col3 = st.columns(3)

col1.metric("Topics in Library", len(TOPICS))
col2.metric("Matching Topics", len(filtered_topics))
col3.metric(
    "Topics with Simulations",
    sum(1 for topic in TOPICS.values() if topic.get("simulation")),
)

if not filtered_topics:
    st.info("No topics match your filters. Try another subject or search term.")
else:
    topic_names = [name for name, _ in filtered_topics]
    selected_topic = st.selectbox("Choose a Chapter or Practical", topic_names)
    selected_data = dict(filtered_topics)[selected_topic]
    render_topic(selected_topic, selected_data)

with st.expander("About This Project"):
    st.write(
        "This app provides concise revision notes and links to external educational "
        "simulations. External simulations are maintained by their providers, and "
        "availability or embedding may change."
    )
