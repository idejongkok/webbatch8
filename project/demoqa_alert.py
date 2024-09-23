from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10) # cukup ditulis sekali aja

driver.maximize_window()
driver.get("https://demoqa.com/alerts")

driver.find_element(By.ID,"alertButton").click()

try:
    WebDriverWait(driver,5).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

except TimeoutException:
    print("alertnya kaga muncul bang")
    
text = driver.find_element(By.XPATH,"//h1[@class='text-center']").text
driver.close()

print(text)