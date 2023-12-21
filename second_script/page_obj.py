import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class SbisPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://sbis.ru/")

    def go_to_contacts_page(self) -> None:
        contact_link = self.driver.find_element(By.XPATH, "//a[@href='/contacts']")
        contact_link.click()

    def get_region_btn(self) -> WebElement:
        return self.driver.find_element(
            By.CSS_SELECTOR, "span.sbis_ru-Region-Chooser__text"
        )

    def get_items_points(self) -> list[WebElement]:
        return self.driver.find_elements(By.XPATH, "//div[@data-qa='item']")

    def change_region_to_kamchatka(self) -> None:
        region_btn = self.get_region_btn()
        region_btn.click()

        self.driver.implicitly_wait(2)

        target_region = self.driver.find_element(
            By.XPATH, '//span[@title="Камчатский край"]'
        )
        target_region.click()
        time.sleep(0.5)
