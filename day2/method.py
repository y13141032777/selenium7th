from day2.logintest import  Login
from selenium import  webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(20)
Login().loginWithDefaultUser(driver)
driver.find_element_by_link_text("账号设置").click()