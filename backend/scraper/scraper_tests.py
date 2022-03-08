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
