import pytest
from selenium.webdriver.remote.webelement import WebElement

from first_script.page_obj import SbisPage, TensorPage
from selenium import webdriver


def check_images_equality(images: list[WebElement]) -> bool:
    first_image_width = images[0].get_attribute("width")
    first_image_height = images[0].get_attribute("height")

    for image in images[1:]:
        if (
            image.get_attribute("width") != first_image_width
            or image.get_attribute("height") != first_image_height
        ):
            return False
    return True


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_scenario_the_whole_script_works(driver):
    sbis_page = SbisPage(driver)
    assert driver.current_url == "https://sbis.ru/"

    sbis_page.go_to_contacts_page()
    assert driver.current_url == "https://sbis.ru/contacts"

    sbis_page.go_to_tensor_website()
    assert driver.current_url == "https://tensor.ru/"

    tensor_page = TensorPage(driver)
    tensor_page.go_to_tensor_about_page()
    assert driver.current_url == "https://tensor.ru/about"

    images = tensor_page.get_images_from_about_page()
    assert check_images_equality(images)
