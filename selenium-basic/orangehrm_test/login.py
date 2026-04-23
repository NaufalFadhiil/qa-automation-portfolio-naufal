from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

username_input = wait.until(
    EC.visibility_of_element_located((By.NAME, "username"))
)
username_input.send_keys("Admin")

password_input = wait.until(
    EC.visibility_of_element_located((By.NAME, "password"))
)
password_input.send_keys("admin123")

time.sleep(1)
driver.quit()