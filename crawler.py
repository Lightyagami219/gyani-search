import json

database=[]

topics=[

# physics
"Newton's laws of motion",
"Law of universal gravitation",
"Thermodynamics",
"Electromagnetism",
"Quantum mechanics",
"Relativity",
"Momentum",
"Kinetic energy",
"Potential energy",
"Wave motion",
"Classical mechanics",
"Angular momentum",
"Force",
"Work and energy",
"Entropy",
"Maxwell equations",
"Planck constant",
"Schrodinger equation",
"Heisenberg uncertainty principle",
"Quantum field theory",

# astronomy
"Black hole",
"Supernova",
"Galaxy",
"Milky Way",
"Dark matter",
"Dark energy",
"Event horizon",
"Neutron star",
"Pulsar",
"Exoplanet",
"Cosmic microwave background",
"Big Bang",
"Inflation theory",
"Cosmic expansion",
"Gravitational waves",
"Space-time",

# biology
"Cell biology",
"DNA",
"RNA",
"Genetics",
"Evolution",
"Natural selection",
"Photosynthesis",
"Respiration",
"Neuron",
"Protein synthesis",
"Enzyme",
"Metabolism",
"Immune system",
"Stem cells",
"Cell division",
"Mitosis",
"Meiosis",

# chemistry
"Atom",
"Molecule",
"Periodic table",
"Hydrogen",
"Helium",
"Carbon",
"Oxygen",
"Nitrogen",
"Covalent bond",
"Ionic bond",
"Organic chemistry",
"Inorganic chemistry",
"Chemical reaction",
"Acid base reaction",
"Redox reaction",
"Catalyst",

# cosmology
"Multiverse theory",
"Cosmic inflation",
"Large scale structure of universe",
"Dark energy density",
"Cosmic background radiation",
]

for topic in topics:

    database.append({
        "title": topic,
        "url": "https://en.wikipedia.org/wiki/" + topic.replace(" ","_"),
        "description": "Scientific topic about " + topic
    })

# create many variations automatically

extra=[]

for item in database:

    words=item["title"].split()

    for w in words:

        extra.append({
            "title": w + " science",
            "url": item["url"],
            "description": item["description"]
        })

database.extend(extra)

with open("gyani_index.json","w") as f:
    json.dump(database,f,indent=2)

print("Indexed pages:",len(database))
