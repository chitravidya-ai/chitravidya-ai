===========================================
COMPLETE UPDATED PROJECT (ONE SINGLE CODE)
Copy everything below and create the files
===========================================

---------- FILE: requirements.txt ----------
streamlit>=1.32.0


---------- FILE: data/topics.py ----------
# data/topics.py
# Complete Class 12 CBSE Theory + Practical topics with free simulations

TOPICS = {
    # ==================== PHYSICS THEORY ====================
    "electric charges and fields": {
        "subject": "Physics",
        "points": [
            "Electric charge is a fundamental property of matter. Like charges repel, unlike charges attract.",
            "Coulomb’s law: F = k × (q₁q₂)/r², where k = 9 × 10⁹ N m²/C².",
            "Electric field (E) due to a point charge: E = kq/r². Direction is away from positive charge.",
            "Electric field lines never intersect and are denser where field is stronger.",
            "Gauss’s theorem: Φ = q_enclosed / ε₀. Useful for symmetric charge distributions."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html",
        "beginner": [
            "Start by placing positive and negative charges.",
            "Observe the field lines and equipotential lines.",
            "Move the test charge to feel the force."
        ]
    },
    "electrostatic potential and capacitance": {
        "subject": "Physics",
        "points": [
            "Electric potential (V) is work done per unit charge. V = kq/r for a point charge.",
            "Potential difference between two points is the work done in moving a unit charge.",
            "Capacitance C = Q/V. For parallel plate capacitor C = ε₀A/d.",
            "Energy stored in a capacitor = ½CV² = Q²/2C.",
            "Dielectrics increase capacitance by a factor of dielectric constant K."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/capacitor-lab-basics/latest/capacitor-lab-basics_en.html",
        "beginner": [
            "Change the plate separation and area and observe capacitance.",
            "Add a dielectric and see the effect on charge and energy."
        ]
    },
    "current electricity": {
        "subject": "Physics",
        "points": [
            "Ohm’s law: V = IR (for ohmic conductors).",
            "Resistance R = ρl/A. Resistivity depends on material and temperature.",
            "Kirchhoff’s current law (KCL) and voltage law (KVL) are used to analyse circuits.",
            "Wheatstone bridge is balanced when P/Q = R/S.",
            "Emf of a cell is the potential difference when no current is drawn."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html",
        "beginner": [
            "Build simple series and parallel circuits.",
            "Use the voltmeter and ammeter to measure values."
        ]
    },
    "moving charges and magnetism": {
        "subject": "Physics",
        "points": [
            "Magnetic force on a moving charge: F = q(v × B).",
            "Force on a current-carrying wire: F = I(l × B).",
            "Biot-Savart law gives magnetic field due to a current element.",
            "Ampere’s circuital law is useful for symmetric current distributions.",
            "Moving coil galvanometer works on the principle of torque on a current loop."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/magnets-and-electromagnets/latest/magnets-and-electromagnets_en.html",
        "beginner": [
            "Observe the magnetic field around a bar magnet and a coil.",
            "Increase current and see the field strength increase."
        ]
    },
    "electromagnetic induction": {
        "subject": "Physics",
        "points": [
            "Faraday’s law: Induced emf = –dφ/dt.",
            "Lenz’s law gives the direction of induced current (opposes the change).",
            "Self inductance L = φ/I. Energy stored = ½LI².",
            "Mutual inductance is the flux linkage in one coil due to current in another.",
            "Eddy currents are induced in bulk conductors and can be reduced by laminations."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html",
        "beginner": [
            "Move the magnet in and out of the coil slowly and quickly.",
            "Observe the direction of induced current."
        ]
    },
    "alternating current": {
        "subject": "Physics",
        "points": [
            "AC voltage varies as V = V₀ sin(ωt).",
            "In pure resistor, current and voltage are in phase.",
            "In pure inductor, current lags voltage by 90°.",
            "In pure capacitor, current leads voltage by 90°.",
            "Resonance occurs in LCR circuit when X_L = X_C. Power factor = cosφ."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/circuit-construction-kit-ac/latest/circuit-construction-kit-ac_en.html",
        "beginner": [
            "Build an AC circuit and observe the phase difference."
        ]
    },
    "ray optics and optical instruments": {
        "subject": "Physics",
        "points": [
            "Mirror formula: 1/v + 1/u = 1/f.",
            "Lens formula: 1/v – 1/u = 1/f.",
            "Magnification m = h′/h = v/u.",
            "Total internal reflection occurs when i > critical angle.",
            "Compound microscope and telescope use combination of lenses."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_en.html",
        "beginner": [
            "Change object distance and observe image formation.",
            "Try both convex and concave lenses."
        ]
    },
    "wave optics": {
        "subject": "Physics",
        "points": [
            "Huygens’ principle explains wavefront propagation.",
            "Young’s double slit experiment proves wave nature of light.",
            "Fringe width β = λD/d.",
            "Diffraction is bending of light around obstacles.",
            "Polarisation proves transverse nature of light waves."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/wave-interference/latest/wave-interference_en.html",
        "beginner": [
            "Observe constructive and destructive interference patterns."
        ]
    },
    "dual nature of radiation and matter": {
        "subject": "Physics",
        "points": [
            "Photoelectric effect: Emission of electrons when light falls on metal.",
            "Einstein’s equation: hν = φ + KE_max.",
            "de Broglie wavelength λ = h/p.",
            "Davisson-Germer experiment confirmed wave nature of electrons.",
            "Wave-particle duality is a fundamental concept of quantum physics."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/photoelectric-effect/latest/photoelectric-effect_en.html",
        "beginner": [
            "Change frequency and intensity and observe the effect on current."
        ]
    },
    "atoms": {
        "subject": "Physics",
        "points": [
            "Rutherford’s model explained nuclear atom but failed for stability.",
            "Bohr’s model: Electrons revolve in discrete orbits. mvr = nh/2π.",
            "Energy of electron in nth orbit: E_n = –13.6/n² eV (for hydrogen).",
            "Spectral lines of hydrogen: Lyman, Balmer, Paschen series.",
            "de Broglie explained Bohr’s quantisation condition."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_en.html",
        "beginner": [
            "Add protons, neutrons and electrons to build different atoms."
        ]
    },
    "nuclei": {
        "subject": "Physics",
        "points": [
            "Mass defect and binding energy explain nuclear stability.",
            "Binding energy per nucleon is maximum around iron.",
            "Radioactive decay: α, β and γ radiation.",
            "Half-life T½ = 0.693/λ.",
            "Nuclear fission and fusion are sources of nuclear energy."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/alpha-decay/latest/alpha-decay_en.html",
        "beginner": [
            "Watch the random nature of radioactive decay."
        ]
    },
    "semiconductor electronics": {
        "subject": "Physics",
        "points": [
            "Intrinsic and extrinsic semiconductors (n-type and p-type).",
            "p-n junction diode: Forward and reverse bias.",
            "Rectifier converts AC to DC (half-wave and full-wave).",
            "Zener diode is used as voltage regulator.",
            "Transistor can work as amplifier and switch."
        ],
        "simulation": None,
        "beginner": []
    },

    # ==================== PHYSICS PRACTICALS ====================
    "meter bridge": {
        "subject": "Physics Practical",
        "points": [
            "Meter bridge is based on Wheatstone bridge principle.",
            "It is used to find unknown resistance.",
            "At balance point: P/Q = R/S where P and Q are ratio arms.",
            "Resistance of wire = (resistance per unit length) × length.",
            "End corrections and resistance of connecting wires should be considered for accuracy."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html",
        "beginner": [
            "Build a Wheatstone bridge circuit using the simulation.",
            "Adjust resistances until galvanometer shows zero deflection."
        ]
    },
    "potentiometer": {
        "subject": "Physics Practical",
        "points": [
            "Potentiometer is used to measure emf and internal resistance of a cell.",
            "It works on the principle that potential difference is proportional to length of wire.",
            "Comparison of emfs of two cells: E1/E2 = l1/l2.",
            "Internal resistance r = R (l1 – l2)/l2.",
            "Potentiometer is preferred over voltmeter because it does not draw current at null point."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html",
        "beginner": [
            "Create a potential divider circuit and observe voltage drop along the wire."
        ]
    },
    "galvanometer resistance": {
        "subject": "Physics Practical",
        "points": [
            "Figure of merit of galvanometer is current required for one division deflection.",
            "Resistance of galvanometer can be found by half-deflection method.",
            "Conversion of galvanometer into ammeter requires low shunt resistance.",
            "Conversion of galvanometer into voltmeter requires high series resistance.",
            "These conversions are important practical experiments in Class 12."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html",
        "beginner": [
            "Use resistors and galvanometer in the circuit simulation to understand shunt and series resistance."
        ]
    },
    "focal length of convex lens": {
        "subject": "Physics Practical",
        "points": [
            "Focal length of convex lens can be found by u-v method.",
            "Lens formula: 1/v – 1/u = 1/f.",
            "Object is placed at different positions and image distance is measured.",
            "Graph between u and v is plotted or calculation is done directly.",
            "Radius of curvature and refractive index can also be related using lens maker’s formula."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_en.html",
        "beginner": [
            "Change object distance and observe image distance.",
            "Note the positions where real image is formed."
        ]
    },
    "refractive index of prism": {
        "subject": "Physics Practical",
        "points": [
            "Refractive index of material of prism μ = sin((A+D)/2) / sin(A/2).",
            "A is angle of prism and D is angle of minimum deviation.",
            "Minimum deviation occurs when angle of incidence equals angle of emergence.",
            "This is a standard Class 12 practical experiment.",
            "Dispersion of light can also be observed with prism."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_en.html",
        "beginner": [
            "Use the prism in the simulation and observe refraction and deviation."
        ]
    },
    "ohms law verification": {
        "subject": "Physics Practical",
        "points": [
            "Ohm’s law states that V ∝ I when temperature is constant.",
            "Graph between V and I is a straight line passing through origin for ohmic conductors.",
            "Slope of V-I graph gives resistance.",
            "This is one of the most basic and important practicals.",
            "Non-ohmic devices do not follow Ohm’s law."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/ohms-law/latest/ohms-law_en.html",
        "beginner": [
            "Change voltage and observe current.",
            "Verify that V/I remains constant."
        ]
    },

    # ==================== CHEMISTRY THEORY ====================
    "solutions": {
        "subject": "Chemistry",
        "points": [
            "Concentration can be expressed as molarity, molality, mole fraction, etc.",
            "Raoult’s law for ideal solutions: p = p⁰ × x.",
            "Colligative properties depend only on number of particles.",
            "Relative lowering of vapour pressure, elevation in boiling point, depression in freezing point, osmotic pressure.",
            "Van’t Hoff factor (i) accounts for association/dissociation."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/concentration/latest/concentration_en.html",
        "beginner": [
            "Change the amount of solute and volume to see concentration change."
        ]
    },
    "electrochemistry": {
        "subject": "Chemistry",
        "points": [
            "Galvanic cell converts chemical energy to electrical energy.",
            "Nernst equation: E = E° – (RT/nF) ln Q.",
            "Standard electrode potential is measured with respect to SHE.",
            "Conductance, specific conductance and molar conductance.",
            "Kohlrausch’s law is used for weak electrolytes."
        ],
        "simulation": None,
        "beginner": []
    },
    "chemical kinetics": {
        "subject": "Chemistry",
        "points": [
            "Rate of reaction depends on concentration, temperature and catalyst.",
            "Order of reaction is experimental; molecularity is theoretical.",
            "Integrated rate equations for zero and first order reactions.",
            "Half-life of first order reaction is independent of initial concentration.",
            "Arrhenius equation: k = Ae^(–Ea/RT)."
        ],
        "simulation": None,
        "beginner": []
    },
    "d and f block elements": {
        "subject": "Chemistry",
        "points": [
            "Transition metals have partially filled d-orbitals.",
            "They show variable oxidation states, coloured ions and catalytic properties.",
            "Lanthanoids show lanthanoid contraction.",
            "Actinoids are radioactive and show more variable oxidation states.",
            "KMnO₄ and K₂Cr₂O₇ are important oxidising agents."
        ],
        "simulation": None,
        "beginner": []
    },
    "coordination compounds": {
        "subject": "Chemistry",
        "points": [
            "Werner’s theory explained primary and secondary valency.",
            "Coordination number is the number of ligands attached to central metal.",
            "IUPAC nomenclature rules for naming complexes.",
            "Isomerism: geometrical, optical, linkage, ionisation etc.",
            "Valence Bond Theory and Crystal Field Theory explain bonding."
        ],
        "simulation": None,
        "beginner": []
    },
    "haloalkanes and haloarenes": {
        "subject": "Chemistry",
        "points": [
            "Haloalkanes contain halogen attached to sp³ carbon.",
            "Nucleophilic substitution can be SN1 or SN2.",
            "Haloarenes are less reactive towards nucleophilic substitution.",
            "Important reactions: Wurtz, Fittig, Hunsdiecker, Sandmeyer.",
            "Polyhalogen compounds like chloroform, DDT, freons have specific uses."
        ],
        "simulation": None,
        "beginner": []
    },
    "alcohols phenols and ethers": {
        "subject": "Chemistry",
        "points": [
            "Alcohols contain –OH group. Phenols are more acidic than alcohols.",
            "Preparation methods: hydration of alkenes, from carbonyl compounds, etc.",
            "Reactions: esterification, dehydration, oxidation.",
            "Phenols give electrophilic substitution reactions easily.",
            "Ethers are prepared by Williamson synthesis."
        ],
        "simulation": None,
        "beginner": []
    },
    "aldehydes ketones and carboxylic acids": {
        "subject": "Chemistry",
        "points": [
            "Carbonyl compounds contain C=O group.",
            "Nucleophilic addition is the characteristic reaction.",
            "Aldehydes are more reactive than ketones.",
            "Carboxylic acids are acidic due to resonance stabilisation of carboxylate ion.",
            "Important tests: Tollens’, Fehling’s, 2,4-DNP."
        ],
        "simulation": None,
        "beginner": []
    },
    "amines": {
        "subject": "Chemistry",
        "points": [
            "Amines are derivatives of ammonia.",
            "Basicity order in aqueous solution: secondary > primary > tertiary (for aliphatic).",
            "Preparation: from nitro compounds, nitriles, amides, etc.",
            "Carbylamine test is used for primary amines.",
            "Diazonium salts are important intermediates for aromatic compounds."
        ],
        "simulation": None,
        "beginner": []
    },
    "biomolecules": {
        "subject": "Chemistry",
        "points": [
            "Carbohydrates are polyhydroxy aldehydes or ketones.",
            "Proteins are polymers of amino acids linked by peptide bonds.",
            "Enzymes are biological catalysts (mostly proteins).",
            "Nucleic acids (DNA & RNA) carry genetic information.",
            "Vitamins are essential organic compounds required in small amounts."
        ],
        "simulation": None,
        "beginner": []
    },

    # ==================== CHEMISTRY PRACTICALS ====================
    "acid base titration": {
        "subject": "Chemistry Practical",
        "points": [
            "Titration is used to find concentration of unknown solution.",
            "Acid-base titration uses indicators like phenolphthalein or methyl orange.",
            "End point is the point at which indicator changes colour.",
            "Molarity equation: M1V1 = M2V2 (for same number of H+ and OH–).",
            "This is one of the most common Class 12 Chemistry practicals."
        ],
        "simulation": "https://phet.colorado.edu/sims/html/acid-base-solutions/latest/acid-base-solutions_en.html",
        "beginner": [
            "Change concentration of acid and base and observe pH.",
            "Understand the concept of strong and weak acids/bases."
        ]
    },
    "ph and indicators": {
        "subject": "Chemistry Practical",
        "points": [
            "pH = –log[H+]. It measures acidity or basicity of solution.",
            "Indicators are weak acids or bases that change colour in specific pH range.",
