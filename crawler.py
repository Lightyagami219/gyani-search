import json
import random

subjects = [
"physics","quantum physics","mechanics","thermodynamics","electromagnetism",
"astronomy","cosmology","astrophysics","particle physics","nuclear physics",
"biology","genetics","cell biology","evolution","microbiology",
"chemistry","organic chemistry","biochemistry"
]

concepts = [
"law","theory","principle","equation","experiment",
"effect","model","process","reaction","mechanism"
]

objects = [
"atom","molecule","black hole","galaxy","neutron star","supernova",
"electron","proton","neutron","cell","dna","rna","enzyme",
"planet","star","cosmic radiation","dark matter","dark energy"
]

database=[]

for i in range(3000):

    title = (
        random.choice(subjects).title() + " " +
        random.choice(concepts).title() + " of " +
        random.choice(objects).title()
    )

    database.append({
        "title": title,
        "url": "https://en.wikipedia.org/wiki/" + title.replace(" ","_"),
        "description": "Scientific topic about " + title
    })

with open("gyani_index.json","w",encoding="utf-8") as f:
    json.dump(database,f,indent=2)

print("Indexed pages:",len(database))
