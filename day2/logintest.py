#打开浏览器
from   selenium import  webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Login:
    def  loginWithDefaultUser(self,driver):

        # driver = webdriver.Chrome()
        #打开海岛上城
        # driver.implicitly_wait(20)

        driver.get("http://172.31.15.27:8081/")
        #删除登陆连接的target属性
        driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
        #点击登陆跳转到登录页面
        driver.find_element_by_link_text("登录").click()

        #输入登录名
        driver.find_element_by_id("username").send_keys("yxg")
        #driver.find_element_by_name("password").send_keys("111111")
        #python 不需要声明变量类型
        action =  ActionChains(driver)
        action.send_keys(Keys.TAB).send_keys("111111").perform()
        #回车登陆
        #action.send_keys(Keys.ENTER).perform()
        #点击登录按钮登陆

        #submit  提交
        driver.find_element_by_id("username").submit()
