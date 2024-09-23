from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10) # cukup ditulis sekali aja

driver.maximize_window()
driver.get("https://demoqa.com/menu")

mainitem2 = driver.find_element(By.XPATH,"//a[normalize-space()='Main Item 2']")
subsublist = driver.find_element(By.XPATH,"//a[normalize-space()='SUB SUB LIST »']")
subsubitem2 = driver.find_element(By.XPATH,"//a[normalize-space()='Sub Sub Item 2']")

action_hover_menu = ActionChains(driver)
action_hover_menu.move_to_element(mainitem2)
action_hover_menu.move_to_element(subsublist)
action_hover_menu.move_to_element(subsubitem2)
action_hover_menu.perform()

print(subsubitem2.text)

driver.close()