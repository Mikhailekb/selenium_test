from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class SbisPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://sbis.ru/")

    def go_to_contacts_page(self) -> None:
        contact_link = self.driver.find_element(By.XPATH, "//a[@href='/contacts']")
        contact_link.click()

    def go_to_tensor_website(self) -> None:
        logo_link = self.driver.find_element(By.XPATH, "//a[@title='tensor.ru']")
        logo_link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])


class TensorPage:
    def __init__(self, driver, is_opened=True):
        self.driver = driver
        if not is_opened:
            self.driver.get("https://tensor.ru/")

    def go_to_tensor_about_page(self) -> None:
        title = self.driver.find_element(
            By.XPATH, "//p[contains(text(), 'Сила в людях')]"
        )
        title_parent = title.find_element(By.XPATH, "..")
        about_link = title_parent.find_element(By.LINK_TEXT, "Подробнее")
        self.driver.execute_script("arguments[0].click();", about_link)

    def get_images_from_about_page(self) -> list[WebElement]:
        images: list[WebElement] = self.driver.find_elements(
            By.CSS_SELECTOR, "img.tensor_ru-About__block3-image"
        )
        return images
