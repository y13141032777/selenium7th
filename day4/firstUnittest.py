#第一个单元测试框架的demo
#要想用使用unittest先导包,unittest在python的SDK中自带的
#根据光标的位置执行测试用例，光标在哪 就执行哪个，如果光标在unittest这个方法  就执行所有的
#重写方法  @classmethod只在类中所有被重写的方法前或者后调用一次
#测试用例一个类中 所有测试用例方法的执行顺序是根据方法名的字母顺序决定的
import  unittest

#创建一个类，用来编写自动化测试用例，这个类需要继承unittest框架中的TestCase这个类
#文件名首字母小写，类名首字母大写
#()表示继承，实意为扩展
class   FirstUintTest(unittest.TestCase):
#   3.重写父类的setUp（初始化，配置测试前提条件）和tearDown(测试用例执行完之后做的操作，比如清除脏数据，还原测试场景发邮件等)方法
    def setUp(self):
        print("默认setup-----")

    def tearDown(self):
        print("默认teardown------")
#框架规定测试用例方法必须以test开头
    def test_login(self):
        print("登陆案例----")
        self.hit()
    def hit(self):
#在python中，每个方法都有一个self关键字，如果想使用类的属性和方法，那么必须在调用前边加self关键字
        print("被调用方法")


    def test_zhuce(self):
        print("注册测试案例----")
    @classmethod
    def setUpClass(cls):
        print("重写setup------")

    @classmethod
    def tearDownClass(cls):
        print("重写teardown--------")

#在程序运行时通过下面的语句判断此文件是否为程序入口
#如果当前文件是程序的入口，那么就会执行if中的字句
    if __name__ == '__main__':
        unittest.main()


