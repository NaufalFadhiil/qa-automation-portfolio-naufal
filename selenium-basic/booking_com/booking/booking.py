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
        try:
            exit_modals = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')))
            print('pop up modal muncul')
            exit_modals.click()
            print('pop up modal berhasil ditutup')
        except Exception as e:
            print(f"Error: {e}")
            pass

    def change_currency(self, currency):
        try:
            change_currency = self.find_element(By.CSS_SELECTOR, '[data-testid="header-currency-picker-trigger"]')
            change_currency.click()
            print('Currency clicked')
        except Exception as e:
            print(f"Error: {e}")
            