from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://saucedemo.com")

# ambil title logo lalu cetak
title_logo = driver.find_element(By.CLASS_NAME,"login_logo").text
print(title_logo)

# input username
driver.find_element(By.ID,"user-name").send_keys("standard_user")

#input password
driver.find_element(By.NAME,"password").send_keys("secret_sauce")

#click login
# driver.find_element(By.XPATH,"//*[@id='login-button']").click()

driver.find_element(By.XPATH,"//input[@data-test='login-button']").click()

# driver.close()