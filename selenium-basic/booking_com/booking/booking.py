import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super().__init__()  # Selenium Manager akan handle driver otomatis
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc, tb):
        if self.teardown:
            self.quit()

    def web_page(self):
        self.get("https://www.booking.com")

    def exit_modals(self):
        exit_modals = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
        ))
        exit_modals.click()

    def change_currency(self, currency = "IDR"):
        change_currency = self.find_element(By.CSS_SELECTOR, '[data-testid="header-currency-picker-trigger"]')
        change_currency.click()

        time.sleep(2),
            
        quit_currency = WebDriverWait(self, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="selection-modal-close"]')
        )) 
        quit_currency.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.NAME, 'ss')
        search_field.clear() 
        search_field.send_keys(place_to_go)

        first_result = WebDriverWait(self, 5).until(
            EC.element_to_be_clickable((By.ID, 'autocomplete-result-0')
        )) 
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR, f'[data-date="{check_out_date}"]')
        check_out_element.click()