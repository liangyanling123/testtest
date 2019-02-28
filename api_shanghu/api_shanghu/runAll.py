import os
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from common import send_email
from common import common
from common import case_generate
from common import report_template
from readConfig import ReadConfig

result_dir = ReadConfig().get_result_dir('result_dir')
result_url = ReadConfig().get_result_dir('result_url')
# 定义报告存放路径
# fp = open('D:\\pythons\\report\\' + now + "result.html", 'wb')
pro_dir = os.path.split(os.path.realpath(__file__))[0]  # 当前文件的路径
now = time.strftime("%Y%m%d_%H%M%S")
report_name = now + '-result.html'
report_path = result_dir + report_name  # 详细测试报告保存路径
report_url = result_url + report_name  # 详细测试报告访问路径
report_title = '商米API详细测试报告'
report_description = '用例执行结果：'


summary_name = now + '-summary.html'
summary_path = result_dir + summary_name
summary_html = open(summary_path, 'w', encoding='utf-8')


def create_suite():
    """设置获取case的文件夹位置及包含case的文件"""
    suite = unittest.TestSuite()
    all_cases = unittest.defaultTestLoader.discover(pro_dir + '/test_case', 'test*.py', top_level_dir=None)
    for case in all_cases:
        suite.addTests(case)
    return suite


def generate_report(report_path, report_title, report_description):
    """校验详细测试报告文件是否生成，以及文件内容是否正确"""
    try:
        if report_name in os.listdir(result_dir):
            # report = open(report_path, 'rb').read()  # 另一种校验方法，内容是否存在
            # if report.find(report_description.encode('utf-8')) >= 1 and report.find(report_title.encode('utf-8')) >= 1
            if common.find_word(report_path, report_title) and common.find_word(report_path, report_description):
                print("\n所有脚本执行完成，报告已生成！")
                return True
            else:
                print("\n脚本执行出错，报告内容错误！")
                return False
        else:
            print("\n脚本执行出错，未生成测试报告！")
            return False
    except Exception as e:
        print("\n脚本执行失败！报错信息如下\n", e)
        return False


import datetime
def main(h=0, m=0):
    while True:
        # 判断是否达到设定时间，例如0:00
        while True:
            now = datetime.datetime.now()
            # 到达设定时间，结束内循环
            if now.hour==h and now.minute==m:
                break
            # 不到时间就等20秒之后再次检测
            time.sleep(50)
        # 做正事，一天做一次


if __name__ == '__main__':

    case_generate.script_generate()  # 生成测试脚本
    result = open(report_path, 'wb')
    runner = HTMLTestRunner(stream=result,
                            title=report_title,
                            description=report_description)
    print("开始执行脚本：")
    result_run = runner.run(create_suite())  # 运行测试用例
    result.close()  # 关闭报告文件

    pass_count = result_run.success_count
    fail_count = result_run.failure_count
    error_count = result_run.error_count
    start_time = runner.getReportAttributes(result_run)[0][1]
    duration = runner.getReportAttributes(result_run)[1][1]
    content = report_template.html_summary_content(pass_count, fail_count, error_count, start_time, duration)
    content_report_path = report_template.html_report_path(report_url)  # 简要测试报告中包含的详情报告地址信息
    summary_html.write(content + content_report_path)  # 生成简要报告包含访问地址
    summary_html.close()

    if generate_report(report_path, report_title, report_description) is True:  # 执行测试完成，报告正确生成
        send_email.send_email(report_url, summary_path, report_path, False)  # 邮件不发送附件
    else:  # 报告生成失败，将详细测试报告额外以附件方式邮件发送
        send_email.send_email(report_url, summary_path, report_path, True)
