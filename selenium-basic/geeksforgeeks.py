from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = options)

driver.get("https://www.geeksforgeeks.org/")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
home_url = driver.current_url

time.sleep(3)

# Locate the input field for search text and enter
search = driver.find_element(By.CLASS_NAME, "HomePageSearchContainer_homePageSearchContainer_container_input__1LS0r")
search.send_keys("Data Structure")
search.send_keys(Keys.ENTER)

time.sleep(3)

# Wait for the search results page to load
wait.until(lambda d: d.current_url != home_url)
driver.get(home_url)

# Click View More
driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[2]/div/div[2]/a[2]/button').click()

# QUIT
time.sleep(3)
driver.quit()