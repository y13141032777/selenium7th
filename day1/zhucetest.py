#打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()
#打开首页
driver.get("http://172.31.15.27:8081/")
#打开注册页面
driver.get("http://172.31.15.27:8081/index.php?m=user&c=public&a=reg")
#输入信息
driver.find_element_by_name("username").send_keys("yxg777")
driver.find_element_by_name("password").send_keys("111111")
driver.find_element_by_name("userpassword2").send_keys("111111")
driver.find_element_by_name("mobile_phone").send_keys("13141032787")
driver.find_element_by_name("email").send_keys("777@qq.com")
driver.find_element_by_class_name("reg_btn").click()