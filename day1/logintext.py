#open brower
from selenium  import webdriver

import time

driver = webdriver.Chrome()
#隐式等待
driver.implicitly_wait(20)
#20秒内只能等待，一旦发现后边的步骤可以执行，则马上执行，若超过20S仍未执行，则报超时错误
# open the URL
driver.get("http://172.31.15.27:8081/")
#open the login  URL
driver.get("http://172.31.15.27:8081/index.php?m=user&c=public&a=login")
#imput  userid and  password
driver.find_element_by_id("username").send_keys("yxg")
driver.find_element_by_name("password").send_keys("111111")
#press the  login   button
#driver.find_element("登　录").click()
driver.find_element_by_class_name("login_btn").click()
#check   whether  ligin successfully
#time.sleep(5)
username_test = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
print(username_test)

#点击  进入商城购物按钮
#driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a").click()
driver.find_element_by_link_text("进入商城购物").click()
#输入搜索条件“iphone”
driver.find_element_by_name("keyword").send_keys("iphone")
#点击搜索按钮
driver.find_element_by_class_name("btn1").click()
#点击第一个搜索结果
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[1]/p/a").click()
#time.sleep()提供了一种固定的时间等待
#time.sleep(5)

#加入购物车
driver.close() #关闭正在工作的当前窗口
driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_id("joinCarButton").click()