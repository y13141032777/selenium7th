#登陆海盗商城
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day2.logintest import Login

driver = webdriver.Chrome()
driver.implicitly_wait(20)
Login().loginWithDefaultUser(driver)
# driver.get("http://172.31.15.27:8081/")
# driver.find_element_by_link_text("登录").click()
# driver.close()
# driver.switch_to.window(driver.window_handles[-1])
# driver.find_element_by_id("username").send_keys("yxg")
# action = ActionChains(driver)
# action.send_keys(Keys.TAB).send_keys("111111").perform()
# driver.find_element_by_id("username").submit()
#点击账号设置
driver.find_element_by_link_text("账号设置").click()
#点击个人资料
driver.find_element_by_link_text("个人资料").click()
#修改真实姓名
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("韩庚")
#修改性别
# driver.find_elements_by_id("xb")[1].click()

# driver.find_element_by_css_selector('[value="2"]').click()
driver.find_element_by_xpath('//*[@value="0"]').click()
#修改生日
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_name("birthday").clear()
driver.find_element_by_name("birthday").send_keys("1990-02-02")
#修改qq
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("123456")
#确定，修改成功
driver.find_element_by_id("qq").submit()
