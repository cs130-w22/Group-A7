import pytest
from main import Scraper

def test_invalid_city():
    s = Scraper()
    s.scrape_restaurant_info("fake_city", "2022-03-15", "2")
    assert s.get_restaurant_times() == {}
    assert s.get_restaurant_hyperlinks() == {}
    assert s.get_restaurant_tags() == {}

def test_invalid_date():
    s = Scraper()
    s.scrape_restaurant_info("Chicago", "1000-00-00", "2")
    assert s.get_restaurant_times() == {}
    assert s.get_restaurant_hyperlinks() == {}
    assert s.get_restaurant_tags() == {}

def test_invalid_seats():
    s = Scraper()
    s.scrape_restaurant_info("Chicago", "2022-03-15", "-1")
    assert s.get_restaurant_times() == {}
    assert s.get_restaurant_hyperlinks() == {}
    assert s.get_restaurant_tags() == {}

def test_invalid_time():
    s = Scraper()
    s.scrape_restaurant_info("Chicago", "2022-03-15", "2", hhtime=-1)
    assert s.get_restaurant_times() == {}
    assert s.get_restaurant_hyperlinks() == {}
    assert s.get_restaurant_tags() == {}

def test_invalid_cuisine():
    s = Scraper()
    s.scrape_restaurant_info("Chicago", "2022-03-15", "2", hhtime=14, cuisine="xyz")
    assert s.get_restaurant_times() == {}
    assert s.get_restaurant_hyperlinks() == {}
    assert s.get_restaurant_tags() == {}

def test_valid_required_parameters():
    s = Scraper()
    s.scrape_restaurant_info("Chicago", "2022-03-15", "2") # these parameters will not succeed after the given date
    times = s.get_restaurant_times()
    assert len(times) > 0
    for k in times.keys():
        for time in times[k]:
            assert "PM" in time or "AM" in time

    hrefs = s.get_restaurant_hyperlinks()
    b_url = "https://www.exploretock.com"
    assert len(hrefs) > 0
    for k in hrefs.keys():
        assert len(hrefs[k]) > len(b_url) and "https://" in hrefs[k]

    tags = s.get_restaurant_tags()
    assert len(tags) > 0 # tags very heavily between restaurants so there is not much else to test here


def test_valid_with_optional_parameters():
    s = Scraper()
    s.scrape_restaurant_info("Chicago", "2022-03-15", "2", hhtime=18, cuisine="american")
    times = s.get_restaurant_times()
    assert len(times) > 0
    for k in times.keys():
        for time in times[k]:
            assert "PM" in time or "AM" in time

    hrefs = s.get_restaurant_hyperlinks()
    b_url = "https://www.exploretock.com"
    assert len(hrefs) > 0
    for k in hrefs.keys():
        assert len(hrefs[k]) > len(b_url) and "https://" in hrefs[k]

    tags = s.get_restaurant_tags()
    assert len(tags) > 0


def test_valid_diff_city_name():
    s = Scraper()
    s.scrape_restaurant_info("Atlanta", "2022-03-15", "2")
    times = s.get_restaurant_times()
    assert len(times) > 0
    for k in times.keys():
        for time in times[k]:
            assert "PM" in time or "AM" in time

    hrefs = s.get_restaurant_hyperlinks()
    b_url = "https://www.exploretock.com"
    assert len(hrefs) > 0
    for k in hrefs.keys():
        assert len(hrefs[k]) > len(b_url) and "https://" in hrefs[k]

    tags = s.get_restaurant_tags()
    assert len(tags) > 0

def test_valid_lowercase_city_name():
    s = Scraper()
    s.scrape_restaurant_info("atlanta", "2022-03-15", "2")
    times = s.get_restaurant_times()
    assert len(times) > 0
    for k in times.keys():
        for time in times[k]:
            assert "PM" in time or "AM" in time

    hrefs = s.get_restaurant_hyperlinks()
    b_url = "https://www.exploretock.com"
    assert len(hrefs) > 0
    for k in hrefs.keys():
        assert len(hrefs[k]) > len(b_url) and "https://" in hrefs[k]

    tags = s.get_restaurant_tags()
    assert len(tags) > 0

def test_valid_spaced_city_name():
    s = Scraper()
    s.scrape_restaurant_info("Los Angeles", "2022-03-15", "2")
    times = s.get_restaurant_times()
    assert len(times) > 0
    for k in times.keys():
        for time in times[k]:
            assert "PM" in time or "AM" in time

    hrefs = s.get_restaurant_hyperlinks()
    b_url = "https://www.exploretock.com"
    assert len(hrefs) > 0
    for k in hrefs.keys():
        assert len(hrefs[k]) > len(b_url) and "https://" in hrefs[k]

    tags = s.get_restaurant_tags()
    assert len(tags) > 0