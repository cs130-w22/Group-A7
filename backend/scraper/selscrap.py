from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def get_scraper_info(c,d,s,q):
    URL = f"https://resy.com/cities/{c}?date={d}&seats={s}&query={q}"

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    browser = webdriver.Chrome(options=options, executable_path='/Users/vedantsathye/Documents/chromedriver')
    browser.get(URL)
    html = browser.page_source
    soup = BeautifulSoup(html, features="html.parser")

    browser.quit()
    m_dict_times = {}
    m_dict_links = {}
    for i in range(5):
        browser = webdriver.Chrome(options=options, executable_path='/Users/vedantsathye/Documents/chromedriver')
        name = str(soup.findAll('h3', class_='SearchResult__venue-name')[i])[37:-5]
        xxx = soup.findAll('div', class_='ScrollTo')[i].find('a', class_="Link SearchResult__container-link", href=True)
        nl = "https://resy.com/" + str(xxx['href'])
        m_dict_links[name] = nl
        browser.get(nl)
        html = browser.page_source
        soup2 = BeautifulSoup(html, features="html.parser")
        ret = []
        for a in soup2.findAll('div', class_="time"):
            ret.append(str(a)[18:-6])
        m_dict_times[name] = ret
        browser.quit()



    browser.quit()
    return (m_dict_times, m_dict_links)
