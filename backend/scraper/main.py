import re

# test input
city = "la"
date = "2022-03-03"
seats = "2"
query = "american"
URL = f"https://resy.com/cities/{city}?date={date}&seats={seats}&query={query}"

from requests_html import AsyncHTMLSession

asession = AsyncHTMLSession()

# scrape Resy for restaurant results
async def get_results():
    r = await asession.get(URL)
    await r.html.arender(wait = 3, sleep = 3)
    return r

# parse restaurant results to get restaurant names
def extract_resy_names(results):
    feed = results[0].html.text
    resy_lines = feed.splitlines()
    resy_names = []
    for i in range(len(resy_lines)):
        revRegex = re.compile(r'\$')
        res = revRegex.search(resy_lines[i])
        if res is not None:
            resy_names.append(resy_lines[i - 5])
    return resy_names

# scrape resy and get 20 restaurant names
r = asession.run(get_results)
names = extract_resy_names(r)
print(names)


