from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = options)

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

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

time.sleep(3)

# Navigate to DevOps page via Tutorials dropdown menu
tutorials = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[text()='Tutorials']"))
)
ActionChains(driver).move_to_element(tutorials).perform()

devops = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "DevOps")))
devops.click() 

driver.get(home_url)

# QUIT
time.sleep(3)
driver.quit()