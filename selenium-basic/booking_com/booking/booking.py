import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super().__init__()
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
            
        quit_currency = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="selection-modal-close"]')
        )) 
        quit_currency.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.NAME, 'ss')
        search_field.clear() 
        search_field.send_keys(place_to_go)

        first_result = WebDriverWait(self, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="autocomplete-result"]')
        ))

        for result in first_result:
            if place_to_go.lower() in result.text.lower():
                result.click()
                break

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR, f'[data-date="{check_out_date}"]')
        check_out_element.click()
        time.sleep(1)

    def select_guest(self, adults, children, children_age, rooms):
        selection_element = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='occupancy-config']"))
        )
        selection_element.click()

        adults_container = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='group_adults']/.."))
        )

        adults_value_element = self.find_element(By.ID, 'group_adults')

        buttons = adults_container.find_elements(By.TAG_NAME, "button")
        decrease_button = buttons[0]
        increase_button = buttons[1]

        while True:
            current_value = int(adults_value_element.get_attribute('value'))
            if current_value == 1:
                break
            decrease_button.click()

        while True:
            current_value = int(adults_value_element.get_attribute('value'))
            if current_value == adults:
                break
            increase_button.click()

        child_container = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='group_children']/.."))
        )

        child_value_element = self.find_element(By.ID, 'group_children')

        buttons = child_container.find_elements(By.TAG_NAME, "button")
        decrease_button = buttons[0]
        increase_button = buttons[1]

        while True:
            current_value = int(child_value_element.get_attribute('value'))
            if current_value == 0:
                break
            decrease_button.click()
        
        while True:
            current_value = int(child_value_element.get_attribute('value'))
            if current_value == children:
                break
            increase_button.click()

        # Children Age Selection
        if children:
            selection_element = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='occupancy-config']"))
            )

            age_selects = WebDriverWait(self, 10).until(
                EC.presence_of_all_elements_located((By.NAME, 'age'))
            )

            assert len(age_selects) == children

            for i in range(children):
                age_selects = WebDriverWait(self, 10).until(
                    EC.presence_of_all_elements_located((By.NAME, 'age'))
                )

                element = age_selects[i]

                WebDriverWait(self, 10).until(
                    EC.element_to_be_clickable(element)
                )

                element.click()

                Select(element).select_by_value(str(children_age[i]))

                WebDriverWait(self, 5).until(
                    lambda d: age_selects[i].get_attribute("value") == str(children_age[i])
                )

                time.sleep(1)

        rooms_input = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.ID, "no_rooms"))
        )

        rooms_container = rooms_input.find_element(By.XPATH, "./ancestor::div[1]")

        buttons = rooms_container.find_elements(By.TAG_NAME, "button")
        decrease_button = buttons[0]
        increase_button = buttons[1]

        get_value = lambda: int(rooms_input.get_attribute("value"))

        while get_value() > 1:
            decrease_button.click()
            time.sleep(0.3)

        while get_value() < rooms:
            increase_button.click()
            time.sleep(0.3)

    # TODO: implement pets switch
    # def click_pets(self):
    #     pets = WebDriverWait(self, 5).until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="pets"]')
    #     )) 
    #     pets.click()

    # TODO: implement done button