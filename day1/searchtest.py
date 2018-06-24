from selenium import  webdriver
driver = webdriver.Chrome()
driver.get("http://172.31.15.27:8081/")
#driver.get("http://172.31.15.27:8081/index.php?m=user&c=public&a=login")
driver.find_element_by_link_text("登录").click()
driver.switch_to.window(driver.window_handles[-1])
#[0]表示第一个  [-1]表示最后一个 [-2]倒数第二个
driver.find_element_by_name("keyword").send_keys("iphone")