from bs4 import BeautifulSoup
from selenium import webdriver

class ResyScraper:
    def __init__(self):
        self.times_dict = dict()
        self.links_dict = dict()

    # acquire restaurant info from Resy
    def get_resy_info(self, c, d, s, q):
        URL = f"https://resy.com/cities/{c}?date={d}&seats={s}&query={q}"

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        try:
            browser = webdriver.Chrome()
            browser.get(URL)
            html = browser.page_source
            soup = BeautifulSoup(html, features="html.parser")

            browser.quit()
            m_dict_times = {}
            m_dict_links = {}
            for i in range(5):
                browser = webdriver.Chrome()
                acquire_names = soup.findAll('h3', class_='SearchResult__venue-name')
                name = str(acquire_names[i])[37:-5]
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
        except:
            return {}, {}

        self.times_dict = m_dict_times
        self.links_dict = m_dict_links

    # get reservation times
    def get_times(self):
        return self.times_dict

    # get restaurant links
    def get_links(self):
        return self.links_dict
