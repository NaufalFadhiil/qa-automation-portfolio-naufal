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

main_tab = driver.current_window_handle

time.sleep(3)

# Locate the input field for search text and enter
search = driver.find_element(By.CLASS_NAME, "HomePageSearchContainer_homePageSearchContainer_container_input__1LS0r")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(3)

# Wait for the search results page to load
wait.until(lambda d: d.current_url != home_url)
driver.get(home_url)

time.sleep(3)

# Click on the first link
driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[2]/div/div[2]/a[5]/button').click()

wait.until(lambda d: len(d.window_handles) > 1)
all_tabs = driver.window_handles
driver.switch_to.window(all_tabs[-1])

time.sleep(3)
driver.switch_to.window(main_tab)

# QUIT
time.sleep(3)
driver.quit()