# import requests
# from bs4 import BeautifulSoup
from requests_html import HTMLSession
# from selenium import webdriver
# import selenium
# import http.client as httplib
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.common.exceptions import WebDriverException
# from datetime import datetime as dt
from bs4 import BeautifulSoup

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

session = HTMLSession()
r = session.get(URL)
print(r.full_text)

# browser = webdriver.Chrome(executable_path='/Users/vedantsathye/Documents/chromedriver')
# browser.delete_all_cookies()
# browser.get(URL)

# nframe = browser.find_element_by_class_name('ScrolTo')
# browser.switch_to_frame(nframe)

# c = browser.page_source
# soup = BeautifulSoup(c, "html.parser")

# all = soup.find_all("div", {"class": "ScrollTo"})
# print(all)
