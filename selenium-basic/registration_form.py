from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)
driver.implicitly_wait(10)

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

time.sleep(1)

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

# Subjects
subjects = ["Computer Science", "Maths", "English", "History"]

subject_input = driver.find_element(By.ID, "subjectsInput")

for sub in subjects:
    subject_input.send_keys(sub)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "subjects-auto-complete__menu"))
    )
    subject_input.send_keys(Keys.ENTER)

# Hobbies 
hobby_map = {
    "Sports": "hobbies-checkbox-1",
    "Reading": "hobbies-checkbox-2",
    "Music": "hobbies-checkbox-3"
}

selected_hobbies = ["Sports", "Reading", "Music"]

for hobby in selected_hobbies:
    driver.find_element(By.ID, hobby_map[hobby]).click()

# Upload Picture
picture = driver.find_element(By.ID, "uploadPicture")
picture.send_keys("C:\Penyimpanan Utama\Downloads\sampleFile.jpeg")

# Address 
addres = driver.find_element(By.ID, "currentAddress")
addres.send_keys("Jl. Cikutra No. 22, RT 05/RW 02, Kota Bandung, Jawa Barat.")

# State 
state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("NCR")
state.send_keys(Keys.ENTER)

# City
city = driver.find_element(By.ID, "react-select-4-input")
city.send_keys("Delhi")
city.send_keys(Keys.ENTER)

# Submit Button
submit = driver.find_element(By.ID, "submit")
submit.click()

time.sleep(10)
driver.quit()