import requests
from bs4 import BeautifulSoup
import json

database = []

def add_result(title, url, description):
    database.append({
        "title": title,
        "url": url,
        "description": description
    })

# ---------- Wikipedia ----------
wiki_topics = [
    "Physics",
    "Biology",
    "Chemistry",
    "Astronomy",
    "Cosmology",
    "Genetics"
]

for topic in wiki_topics:

    url = f"https://en.wikipedia.org/wiki/{topic}"

    r = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(r.text,"html.parser")

    for link in soup.select("a[href^='/wiki/']")[:200]:

        href = link.get("href")

        if ":" not in href:

            full = "https://en.wikipedia.org" + href
            title = href.replace("/wiki/","")

            add_result(title, full, "Wikipedia science page")

# ---------- NASA ----------
try:
    nasa = requests.get("https://www.nasa.gov/")
    soup = BeautifulSoup(nasa.text,"html.parser")

    for link in soup.find_all("a"):

        href = link.get("href")

        if href and "nasa.gov" in href:

            add_result(link.text.strip(), href, "NASA science article")

except:
    pass


# ---------- arXiv papers ----------
try:
    arxiv = requests.get("https://arxiv.org/list/astro-ph/new")
    soup = BeautifulSoup(arxiv.text,"html.parser")

    for link in soup.find_all("a", title="Abstract"):

        paper = "https://arxiv.org" + link.get("href")

        add_result("arXiv Research Paper", paper, "Scientific research paper")

except:
    pass


# ---------- Save index ----------
with open("gyani_index.json","w",encoding="utf-8") as f:
    json.dump(database,f,indent=2,ensure_ascii=False)

print("Indexed pages:", len(database))
