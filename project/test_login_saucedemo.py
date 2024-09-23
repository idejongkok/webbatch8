from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def setup_teardown():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    
    #precondition
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://saucedemo.com")
    
    yield driver
    
    #post condition
    driver.close()    
    
    
def test_login_positive(setup_teardown):
    
    setup_teardown.find_element(By.ID,'user-name').send_keys('standard_user')
    setup_teardown.find_element(By.ID,'password').send_keys('secret_sauce')
    setup_teardown.find_element(By.ID,'login-button').click()
    
    #masuk ke product page
    title = setup_teardown.find_element(By.XPATH,"//span[@class='title']").text
    
    # assertion / expectation / match process
    
    assert title == 'Products'


error_sample = [('standard_user','salah','Epic sadface: Username and password do not match any user in this service'),
                ('locked_out_user','secret_sauce','Epic sadface: Sorry, this user has been locked out.'),
                ('salah','secret_sauce','Epic sadface: Username and password do not match any user in this service'),
                ('','secret_sauce','Epic sadface: Username is requireds')]

@pytest.mark.parametrize('username,password,error_message',error_sample) 
   
def test_login_error(setup_teardown,username,password,error_message):

    setup_teardown.find_element(By.ID,'user-name').send_keys(username)
    setup_teardown.find_element(By.ID,'password').send_keys(password)
    setup_teardown.find_element(By.ID,'login-button').click()
    
    #masuk ke product page
    error = setup_teardown.find_element(By.XPATH,"//h3[@data-test='error']").send_keys('')
    

    
    # assertion / expectation / match process
    assert error == error_message
