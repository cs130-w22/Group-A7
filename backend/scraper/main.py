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
    global city 
    global date 
    global seats 
    global query 
    global URL 
    r = await asession.get(URL)
    await r.html.arender(wait = 3, sleep = 3)
    return r

# parse restaurant results to get restaurant names
def extract_resy_names(results):
    resy_lines = results.splitlines()
    resy_names = []
    for i in range(len(resy_lines)):
        revRegex = re.compile(r'\$')
        res = revRegex.search(resy_lines[i])
        if res is not None:
            resy_names.append(resy_lines[i - 5])
    return resy_names



def cleanser(places, text):
    delimeters = '|'.join(places)
    m_dict = {}

    for r in places:
        for i in re.split(delimeters, text):
            if 'PM' in i or 'AM' in i:
                for line in i.split('\n'):
                    if 'PM' in line or 'AM' in line:
                        if r in m_dict:
                            m_dict[r].append(line)
                        else:
                            m_dict[r] = [line]
        m_dict[r] = list(set(m_dict[r]))
    return m_dict

def get_scraper_info(c,d,s,q):
    # scrape resy and get 20 restaurant names
    global city 
    global date 
    global seats 
    global query 
    global URL 
    city = c
    date = d
    seats = s
    query = q
    URL = f"https://resy.com/cities/{city}?date={date}&seats={seats}&query={query}"
    r = asession.run(get_results)
    latter = r[0].html.text.split("Guests")
    former = latter[-1].split("‹")[0]
    names = extract_resy_names(former)

    return cleanser(names, former)







