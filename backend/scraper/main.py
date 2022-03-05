# import requests
# from bs4 import BeautifulSoup
# from requests_html import HTMLSession
# # from selenium import webdriver
# # import selenium
# # import http.client as httplib
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.common.exceptions import TimeoutException
# # from selenium.common.exceptions import NoSuchElementException
# # from selenium.common.exceptions import StaleElementReferenceException
# # from selenium.common.exceptions import WebDriverException
# # from datetime import datetime as dt
import re

city = "ny"
date = "2022-03-03"
seats = "2"
query = "mexican"
URL = f"https://resy.com/cities/{city}?date={date}&seats={seats}&query={query}"
# print(URL)

# page = requests.get(URL)
# print(page.content)
# soup = BeautifulSoup(page.content, "html.parser")
# divs = soup.findAll(class_= "ScrollTo")
# print(divs)

# session = HTMLSession()
# r = session.get(URL)
# scrollto =  r.html.find('ScrollTo')
# print(scrollto)

# browser = webdriver.Chrome(executable_path='/Users/vedantsathye/Documents/chromedriver')
# browser.delete_all_cookies()
# browser.get(URL)

# nframe = browser.find_element_by_class_name('ScrolTo')
# browser.switch_to_frame(nframe)

# c = browser.page_source
# soup = BeautifulSoup(c, "html.parser")

# all = soup.find_all("div", {"class": "ScrollTo"})
# print(all)


# from selenium import webdriver
# driver = webdriver.PhantomJS()
# driver.get(URL)
# p_element = driver.find_element_by_class_name(class_='ScrollTo')
# print(p_element)

from requests_html import AsyncHTMLSession

asession = AsyncHTMLSession()

# scrape Resy for restaurant results
async def get_results():
    r = await asession.get(URL)
    await r.html.arender(wait = 3, sleep = 3)
    return r
r = asession.run(get_results)

#
feed = r[0].html.text
resy_lines = feed.splitlines()
c = 0
for l in resy_lines:
    revRegex = re.compile(r'\d.\d\(\d+.*\d*k*\)')
    res = revRegex.search(l)
    if res is not None:
        print(res.group())
        c += 1
print(c)