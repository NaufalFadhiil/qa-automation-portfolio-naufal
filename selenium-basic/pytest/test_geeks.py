from selenium import webdriver

def test_geeks():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://geeksforgeeks.org")
    print("Title: ", driver.title)
    driver.quit()

def test2_lambdatest_ecommerce():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    print("Title: ", driver.title)
    driver.quit()