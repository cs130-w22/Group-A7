import requests
from bs4 import BeautifulSoup


def get_restaurant_info(city_hyphened, city_spaced, date, size):
    url = f"https://www.exploretock.com/city/{c1}/search?city={c2}&date={date}&size={size}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    restaurants = dict()
    search_block = soup.find('div',
                             class_='AvailabilitySearch-destinationResultList AvailabilitySearch-destinationResultList--simple')
    if search_block is None:
        return {}
    search_list = search_block.findAll('li', attrs={'data-businessid': True})
    if search_list is None:
        return {}

    for i in range(len(search_list)):
        name_slot = \
        soup.findAll('h2', class_='MuiTypography-root jss5 jss31 jss21 css-0 MuiTypography-body1 MuiTypography-noWrap')[
            i]
        name = name_slot.getText()

        times = []
        for sl in search_list[i]:
            time_slots = sl.findAll('button', attrs={'data-testid': 'select-time'})
            for ts in time_slots:
                times.append(ts.getText())

        restaurants[name] = times
    return restaurants

# test
#c1 = "los-angeles"
#c2 = "Los Angeles"
#date = "2022-03-07"
#size = "2"
#print(get_restaurant_info(c1, c2, date, size))