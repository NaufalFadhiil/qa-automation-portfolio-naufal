from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, star_value: int):
        star_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//label[.//div[contains(text(), '{star_value} star')]]"
                )
            )
        )
        star_option.click()

    def sort_lowest_price(self):
        sort_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-testid="sorters-dropdown-trigger"]')
            )
        )
        sort_element.click()

        sort_price = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-id="price"]')
            )
        )
        sort_price.click()

    def click_first_hotel(self):
        first_hotel = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    '[data-testid="property-card"] [data-testid="title-link"]'
                )
            )
        )
        first_hotel.click()
