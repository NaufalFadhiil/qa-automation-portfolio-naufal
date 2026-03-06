from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = options)

for i in range(2): # Loop 2 kali untuk pop up yg tidak selalu muncul
    driver.get("https://tees.co.id")
    
    # Tunggu sampai pop up muncul
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]')))
        print("pop up modal muncul")

        driver.find_element(By.CLASS_NAME, "btn-modal-close").click()
        print("pop up modal berhasil ditutup")

    except TimeoutException:
        print("pop up modal tidak muncul")
        pass

driver.quit()