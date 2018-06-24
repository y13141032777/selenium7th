# 要想读取csv文件，首先导入csv代码库
# csv包很常用，python包自带的，不用下载，用excle就需要下载代码库xlrd（下载方法1.通过命令下载，在dos窗口输入pip install -U xlrd）
# pip:python常用的项目管理工具
# -U：升级到最新版本
# xlrd： 包名
import  csv

# path ="C:\\Users\\51Testing\\PycharmProjects\\selenium7th\\data\\tsetdata.csv"

# path ="C:/Users/51Testing/PycharmProjects/selenium7th/data/tsetdata.csv"

path = r"C:\Users\51Testing\PycharmProjects\selenium7th\data\tsetdata.csv"
print(path)

file = open(path,"r")

data_table= csv.reader(file)

# item代表每一行，每循环一次item就代表最新的一行数据
for item in data_table:
    print(item)