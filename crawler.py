import requests
from bs4 import BeautifulSoup
import json
from collections import deque

headers = {
    "User-Agent": "Mozilla/5.0"
}

seed_urls = [
    "https://en.wikipedia.org/wiki/Physics",
    "https://en.wikipedia.org/wiki/Biology",
    "https://en.wikipedia.org/wiki/Chemistry",
    "https://en.wikipedia.org/wiki/Cosmology"
]

visited = set()
queue = deque(seed_urls)
database = []

max_pages = 500

while queue and len(visited) < max_pages:

    url = queue.popleft()

    if url in visited:
        continue

    try:
        print("Crawling:", url)

        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else url

        description = ""
        p = soup.find("p")
        if p:
            description = p.text.strip()

        database.append({
            "title": title,
            "url": url,
            "description": description
        })

        visited.add(url)

        for link in soup.find_all("a", href=True):

            href = link["href"]

            if href.startswith("/wiki/") and ":" not in href:

                full_url = "https://en.wikipedia.org" + href

                if full_url not in visited:
                    queue.append(full_url)

    except Exception as e:
        print("Error:", e)


print("Indexed pages:", len(database))

with open("gyani_index.json", "w", encoding="utf-8") as f:
    json.dump(database, f, indent=2, ensure_ascii=False)
