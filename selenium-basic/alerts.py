from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Tidak auto close browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = options)
driver.get("https://demoqa.com/alerts")

# Normal alert
driver.find_element(By.ID, "alertButton").click()
time.sleep(2)

driver.switch_to.alert.accept()
time.sleep(3)


# Button alert 5 detik
driver.find_element(By.ID, "timerAlertButton").click()
time.sleep(5)

time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(3)


# Cpmfirm alert
driver.find_element(By.ID, "confirmButton").click()
time.sleep(2)

#Untuk mengambil Window Alert
driver.switch_to.alert.dismiss()
time.sleep(3)


# Prompt alert
driver.find_element(By.ID, "promtButton").click()
time.sleep(2)

driver.switch_to.alert.send_keys("JAWAJAWA")
time.sleep(3)

driver.switch_to.alert.accept()
time.sleep(3)

driver.quit()