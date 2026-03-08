from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)
driver.implicitly_wait(10)

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

time.sleep(3)

# Name input
firstName = driver.find_element(By.ID, "firstName")
firstName.send_keys("Naufal")

lastName = driver.find_element(By.ID, "lastName")
lastName.send_keys("Fadhiil")

# User Email
userEmail = driver.find_element(By.ID, "userEmail")
userEmail.send_keys("naufal@example.com")

# Gender
gender = driver.find_element(By.ID, "gender-radio-1")
gender.click()

# Mobile Number 
mobileNumber = driver.find_element(By.ID, "userNumber")
mobileNumber.send_keys("1234567890")

# Date of Birth
dateInput = driver.find_element(By.ID,"dateOfBirthInput")
dateInput.click()
month = driver.find_element(By.CLASS_NAME,"react-datepicker__month-select")
month.send_keys("June")
year = driver.find_element(By.CLASS_NAME,"react-datepicker__year-select")
year.send_keys("2005")
day = driver.find_element(By.XPATH,"//div[contains(@class,'react-datepicker__day') and text()='22']")
day.click()

# TODO: Implement Subjects field
# TODO: Implement Hobbies field
# TODO: Implement Picture field
# TODO: Implement Address field
# TODO: Implement State field
# TODO: Implement City field

time.sleep(5)
driver.quit()