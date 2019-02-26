import os
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from common import send_email
from common import common
from common import case_generate


# # 定义报告存放路径
# # fp = open('D:\\pythons\\report\\' + now + "result.html", 'wb')
# pro_dir = os.path.split(os.path.realpath(__file__))[0]  # 当前文件的路径
# now = time.strftime("%Y%m%d_%H%M%S")
# report_name = now + '-result.html'
# report_path = pro_dir + '/result/' + report_name
# report_title = '商米API测试报告'
# report_description = '用例执行情况：'
#
#
# def create_suite():
#     """设置获取case的文件夹位置及包含case的文件"""
#     suite = unittest.TestSuite()
#     all_cases = unittest.defaultTestLoader.discover(pro_dir + '/test_case', 'test*.py', top_level_dir=None)
#     for case in all_cases:
#         suite.addTests(case)
#     return suite
#
#
# result = open(report_path, 'wb')
# runner = HTMLTestRunner(stream=result,
#                         title=report_title,
#                         description=report_description)
#
# test = create_suite()
# resul = runner.run(create_suite())
# print(str(resul), '\n', runner.getReportAttributes(resul), '\n', resul.success_count, resul.error_count, resul.failure_count)

# from selenium import webdriver
#
# print("start....\n")
# driver = webdriver.PhantomJS()
# url = r"file:///C:/Users/Administrator/PycharmProjects/api_test/result/20181107_181356-summary.html"
# driver.get(url)
# driver.save_screenshot("sohu.png")
# print("ok!\n")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

url = r"file:///C:/Users/Administrator/PycharmProjects/api_test/result/20181107_235851-summary.html"
driver.get(url)
driver.set_window_size(1500, 700)
driver.save_screenshot("sohu1.png")  # 只能对屏幕进行截图

im = Image.open("sohu1.png")
box = (0, 0, 1500, 600)  # 元组参数包含四个值，分别代表矩形四条边的距离X轴或者Y轴的距离，矩形边顺序是(左，顶，右，底)
region = im.crop(box)  # 对图片进行截取
region.save('new.png')


print("ok!\n")

