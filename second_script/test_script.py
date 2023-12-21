import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

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

    sbis_page.go_to_contacts_page()
    assert driver.current_url == "https://sbis.ru/contacts"

    region_btn = sbis_page.get_region_btn()
    region = get_region_name()
    # Проверка, что регион совпадает с текстом на кнопке выбора региона
    assert region in region_btn.text

    assert sbis_page.get_items_points()

    sbis_page.change_region_to_kamchatka()

    region_btn = sbis_page.get_region_btn()
    city_name = driver.find_element(By.ID, "city-id-2")
    current_url = driver.current_url
    title = driver.title

    assert region_btn.text == "Камчатский край"
    assert city_name.text == "Петропавловск-Камчатский"
    assert current_url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"
    assert title == "СБИС Контакты — Камчатский край"
