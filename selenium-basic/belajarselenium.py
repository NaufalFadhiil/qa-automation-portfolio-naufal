from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = options)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(by=By.ID, value="username")
username.send_keys("Naufal")

password = driver.find_element(by=By.ID, value="password")
password.send_keys("123456")

button = driver.find_element(by=By.CLASS_NAME, value="radius")
button.click()

link = driver.find_element(by=By.LINK_TEXT, value="Elemental Selenium")
link.click()

time.sleep(3)
driver.quit()