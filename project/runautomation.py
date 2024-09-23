from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver2 = webdriver.Firefox()

driver.maximize_window()
driver.get('https://idejongkok.com')
print(driver.title)
driver.close()

driver2.get("https:google.com")
print(driver2.title)
driver2.close()