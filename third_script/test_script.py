from pathlib import Path

import pytest
import requests
from selenium import webdriver

from page_obj import SbisPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def get_region_name():
    response = requests.get("http://api.sypexgeo.net/").json()
    region: str = response["region"]["name_ru"]
    return region.split()[0]


def test_scenario_the_whole_script_works(driver):
    sbis_page = SbisPage(driver)
    assert driver.current_url == "https://sbis.ru/"

    sbis_page.go_to_download_page()
    assert driver.current_url == "https://sbis.ru/download?tab=plugin&innerTab=default"
    sbis_page.download_plugin()

    current_directory = Path.cwd()
    exe_file = list(current_directory.glob("*.exe"))
    assert exe_file
