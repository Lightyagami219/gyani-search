import json

topics = [

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

# chemistry
"Atom",
"Molecule",
"Periodic table",
"Hydrogen",
"Oxygen",
"Carbon",
"Covalent bond",
"Ionic bond",
"Organic chemistry",
"Inorganic chemistry",

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

# astronomy
"Black hole",
"Supernova",
"Galaxy",
"Milky Way",
"Dark matter",
"Dark energy",
"Event horizon",
"Neutron star",
"Exoplanet",
"Cosmic microwave background",

# cosmology
"Big Bang",
"Inflation theory",
"Cosmic expansion",
"Multiverse theory",
"Space-time",
"Gravitational waves",
]

database=[]

for topic in topics:

    database.append({
        "title": topic,
        "url": "https://en.wikipedia.org/wiki/" + topic.replace(" ","_"),
        "description": "Scientific topic about " + topic
    })

with open("gyani_index.json","w") as f:
    json.dump(database,f,indent=2)

print("Indexed pages:",len(database))
