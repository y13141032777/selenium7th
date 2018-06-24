#1.导包
import  unittest
#建类继承unittest
from selenium import webdriver

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # 窗口最大化要求驱动版本和浏览器版本精准匹配
        # self.driver.maximize_window()
    @classmethod
    def tearDownClass(self):

        time.sleep(20)
        # 关闭浏览器，清除缓存为下次测试做准备
        # driver是在setup方法里定义的局部变量，局部变量不嗯能够被其他方法访问，所以应该吧driver改成全局变量--self.driver
        # self.driver.quit()


    def test_a_login(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys("\tpassword").send_keys("\t1234").send_keys("\n").perform()
    def test_b_add_prodect(self):
        driver = self.driver
        driver.find_element_by_link_text("商品管理").click()
        driver.find_element_by_link_text("添加商品").click()
        #         除了用name属性切换frame,也可通过8种元素定位方法定位元素,然后切换
        iframe = driver.find_element_by_id("mainFrame")
        driver.switch_to.frame(iframe)
        #         等于driver.switch_to.frame(frame的名字)
        driver.find_element_by_name("name").send_keys("饮水机")
        # 变量名文件名的起名规则:数字,大小写字母,下划线,一般要求以字母开头
        # 如果id是纯数字,用#井号的方式不能定位,
        # 可以用[]的方式定位,所有的属性都可以用[]定位
        driver.find_element_by_css_selector('[id="1"]').click()
        driver.find_element_by_id('2').click()
        driver.find_element_by_id("6").click()
        # driver.find_element_by_id("7").click()
        ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
        select = Select(driver.find_element_by_name("brand_id"))
        select.select_by_value("1")
        driver.find_element_by_class_name("button_search").click()
        # 添加商品代码

#顶格写
if __name__ == '__main__':
    unittest.main()

# 后台地址 http://localhost/index.php?m=admin&c=public&a=login