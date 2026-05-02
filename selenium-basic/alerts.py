from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

# Tidak auto close browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = options)
driver.get("https://demoqa.com/alerts")

# 1. Normal alert
driver.find_element(By.ID, "alertButton").click()
time.sleep(2)

driver.switch_to.alert.accept()
time.sleep(3)


# 2. Button alert 5 detik
driver.find_element(By.ID, "timerAlertButton").click()

#
try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("Alert berhasil muncul")
except TimeoutException:
    print("Tidak ada alert")

time.sleep(3)


# 3. Comfirm alert
driver.find_element(By.ID, "confirmButton").click()
time.sleep(2)

#Untuk mengambil Window Alert
driver.switch_to.alert.dismiss()
time.sleep(3)


# 4. Prompt alert
driver.find_element(By.ID, "promtButton").click()
time.sleep(2)

driver.switch_to.alert.send_keys("JAWAJAWA")
time.sleep(3)

driver.switch_to.alert.accept()
time.sleep(3)

driver.quit()