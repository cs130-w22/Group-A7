import requests
from bs4 import BeautifulSoup


city = "ny"
date = "2022-02-11"
seats = "2"
query = "mexican"
URL = f"https://resy.com/cities/{city}?date={date}&seats={seats}&query={query}"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ScrollTo")

print(results.prettify())
