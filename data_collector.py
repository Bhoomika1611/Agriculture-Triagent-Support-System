import requests
from bs4 import BeautifulSoup
import os

os.makedirs("data", exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0"
}

# more pages to scrape
urls = [
    "https://www.fao.org/agriculture/en/",
    "https://www.fao.org/family-farming/en/",
    "https://www.fao.org/climate-change/en/",
    "https://agriwelfare.gov.in/en/major",
    "https://agriwelfare.gov.in/en/schemes",
]

all_text = []

for url in urls:

    print("Scraping:", url)

    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, "html.parser")

        # headings
        for tag in soup.find_all(["h1","h2","h3","h4"]):
            text = tag.get_text(strip=True)

            if len(text) > 10:
                all_text.append(text)

        # paragraphs
        for tag in soup.find_all("p"):
            text = tag.get_text(strip=True)

            if len(text) > 20:
                all_text.append(text)

        # lists
        for tag in soup.find_all("li"):
            text = tag.get_text(strip=True)

            if len(text) > 20:
                all_text.append(text)

    except Exception as e:
        print("Error:", e)


# remove duplicates
all_text = list(set(all_text))

# save file
file_path = "data/agriculture_docs.txt"

with open(file_path, "w", encoding="utf-8") as f:

    for line in all_text:
        f.write(line + "\n")


print("\nScraping Completed")
print("Total lines saved:", len(all_text))
print("Saved to:", file_path)