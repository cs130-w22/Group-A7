import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        self.base_url = "https://www.exploretock.com"
        self.reservations = dict()
        self.hyperlinks = dict()
        self.tags = dict()

    # scrape restaurant names and reservation times for given search parameters
    def scrape_restaurant_info(self, city, date, size, hhtime=None, cuisine=None):
        """
        Method to
        Receives: restaurant reservation query parameters - city, date, size, time in HH format (optional),
        cuisine (optional)
        Returns: Void; stores reservation times, hyperlinks, and descriptive tags for discovered restaurants
        """
        # set params and url
        city_spaced = city.title()
        city_hyphened = city.lower().replace(" ", "-")
        url = f"https://www.exploretock.com/city/{city_hyphened}/search?city={city_spaced}&date={date}&size={size}"

        url_time = ""
        if hhtime is not None:
            url_time = f"&time={hhtime}"
        url_cuisine = ""
        if cuisine is not None:
            url_cuisine = f"&cuisines={cuisine}"
        url = url + url_time + url_cuisine
        print(url)

        # set up scraping
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        search_block = soup.find('div',
                                 class_='AvailabilitySearch-destinationResultList AvailabilitySearch-destinationResultList--simple')
        if search_block is None:
            return {}
        search_list = search_block.findAll('li', attrs={'data-businessid': True})
        if search_list is None:
            return {}

        # scrape
        time_dict = dict()
        tag_dict = dict()
        href_dict = dict()
        for i in range(len(search_list)):
            # access name
            name_slot = \
                soup.findAll('h2',
                             class_='MuiTypography-root jss5 jss31 jss21 css-0 MuiTypography-body1 MuiTypography-noWrap')[
                    i]
            name = name_slot.getText()

            # access reservation times
            times = []
            for sl in search_list[i]:
                time_slots = sl.findAll('button', attrs={'data-testid': 'select-time'})
                for ts in time_slots:
                    time = ts.getText()
                    if time not in times:
                        times.append(time)
            time_dict[name] = times

            # access restaurant tags
            tag_slot = soup.findAll(
                'p', class_='MuiTypography-root jss5 jss46 jss21 css-0 MuiTypography-body1 MuiTypography-noWrap')[i]
            tag_dict[name] = tag_slot.getText()

            # access restaurant hyperlinks
            href = soup.findAll('a', class_='jss85 Anchor')[i]
            href_dict[name] = self.base_url + href['href']

        self.reservations = time_dict
        self.tags = tag_dict
        self.hyperlinks = href_dict
        return self.reservations

    # get reservation times
    def get_restaurant_times(self):
        """
        Method to
        Receives: No parameters
        Returns: Available reservation times
        """
        return self.reservations

    # get restaurant tags
    def get_restaurant_tags(self):
        """
        Method to
        Receives: No parameters
        Returns: Restaurant descriptive tags
        """
        return self.tags

    # get restaurant hyperlinks
    def get_restaurant_hyperlinks(self):
        """
        Method to
        Receives: No parameters
        Returns: Hyperlinks to restaurants
        """
        return self.hyperlinks