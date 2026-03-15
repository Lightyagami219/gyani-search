import requests
from bs4 import BeautifulSoup
import json

seed_urls = [
    "https://en.wikipedia.org/wiki/Physics",
    "https://en.wikipedia.org/wiki/Biology",
    "https://en.wikipedia.org/wiki/Chemistry",
    "https://en.wikipedia.org/wiki/Cosmology"
]

visited = set()
database = []

for url in seed_urls:

    try:
        print("Crawling:", url)

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a"):

            href = link.get("href")

            if href and href.startswith("/wiki/"):

                full_url = "https://en.wikipedia.org" + href

                if full_url not in visited:

                    visited.add(full_url)

                    title = href.replace("/wiki/", "")

                    database.append({
                        "title": title,
                        "url": full_url,
                        "description": "Wikipedia science page"
                    })

    except:
        pass


with open("gyani_index.json", "w") as f:
    json.dump(database, f, indent=2)

print("Indexed pages:", len(database))
