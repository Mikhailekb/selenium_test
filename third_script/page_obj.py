import time

import requests
from selenium.webdriver.common.by import By


class SbisPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://sbis.ru/")
        time.sleep(1)

    def go_to_download_page(self) -> None:
        download_page = self.driver.find_element(
            By.XPATH, "//a[contains(text(), 'Скачать СБИС')]"
        )
        self.driver.execute_script("arguments[0].click();", download_page)
        time.sleep(1)

        plugin_tab = self.driver.find_element(
            By.XPATH, "//div[contains(text(), 'СБИС Плагин')]"
        )
        self.driver.execute_script("arguments[0].click();", plugin_tab)

    def download_plugin(self) -> None:
        if (
            self.driver.current_url
            != "https://sbis.ru/download?tab=plugin&innerTab=default"
        ):
            self.go_to_download_page()

        web_installer_title = self.driver.find_element(
            By.XPATH, "//h3[contains(text(), 'Веб-установщик')]"
        )

        web_installer_block = web_installer_title.find_element(By.XPATH, "../..")
        download_link = web_installer_block.find_element(
            By.PARTIAL_LINK_TEXT, "Скачать"
        )
        download_link_file = download_link.get_attribute("href")

        response = requests.get(download_link_file)
        file_name = response.url.split("/")[-1]

        with open(file_name, "wb") as file:
            file.write(response.content)
