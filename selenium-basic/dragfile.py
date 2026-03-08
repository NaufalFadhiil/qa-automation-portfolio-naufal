from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)

driver.get("https://demoqa.com/droppable")
driver.maximize_window()

time.sleep(3)

itemDrag = driver.find_element(By.ID, "draggable")
itemDrop = driver.find_element(By.ID, "droppable")

# ActionChains(driver).move_to_element(driver.find_element(By.ID, "draggable"), driver.find_element(By.ID, "droppable")).perform()

actions = ActionChains(driver)

actions.click_and_hold(itemDrag).move_to_element(itemDrop).release().perform()
