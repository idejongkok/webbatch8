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
driver.get("https://demoqa.com/modal-dialogs")

# pencet button trigger untuk large modal
driver.find_element(By.XPATH,"//button[@id='showLargeModal']").click()

try:
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"example-modal-sizes-title-lg")))
    modaltext = driver.find_element(By.ID,"example-modal-sizes-title-lg").text
    print(modaltext)
    
except TimeoutException:
    print('elementnya kaga muncul bang')
                                      
driver.find_element(By.ID,"closeLargeModal").click()

driver.close()