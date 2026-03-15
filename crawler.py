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

headers = {
    "User-Agent": "GYANI-Bot"
}

for url in seed_urls:

    print("Crawling:", url)

    try:

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string

        database.append({
            "title": title,
            "url": url,
            "description": "Science topic",
            "keywords": title.lower()
        })

        for link in soup.find_all("a"):

            href = link.get("href")

            if href and href.startswith("/wiki/"):

                full_url = "https://en.wikipedia.org" + href

                if full_url not in visited:

                    visited.add(full_url)

                    database.append({
                        "title": href.replace("/wiki/", ""),
                        "url": full_url,
                        "description": "Wikipedia science page",
                        "keywords": href.lower()
                    })

    except Exception as e:
        print("Error:", e)

# save database

with open("gyani_index.json", "w") as f:
    json.dump(database, f, indent=2)

print("Indexed pages:", len(database))
