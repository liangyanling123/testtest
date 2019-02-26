
import unittest
from common import configHttp
from common import common
from common.common import get_response as response
from common.special import mgt_admin_id as mgt
from common.special import partner_admin_id as partner

  
class Employee(unittest.TestCase):  # class_name.title()方法为字符串首字母大写
    """人员管理"""
    def setUp(self):
        print("\ncase start!\n")

    def tearDown(self):
        print("\ncase end!\n"
              "*****************************************************************************")
        pass
    
    def test_getsnemployeelist_01(self):
        """获取店铺下的人员列表"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getsnemployeelist_01")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsnemployeelist_02(self):
        """缺失page_num必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getsnemployeelist_02")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsnemployeelist_03(self):
        """缺失page_size必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getsnemployeelist_03")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsnemployeelist_04(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getsnemployeelist_04")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsnemployeelist_05(self):
        """缺失token必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getsnemployeelist_05")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsnemployeelist_06(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getsnemployeelist_06")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsnemployeelist_07(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getsnemployeelist_07")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getemployeedetail_08(self):
        """店长查看店员详情"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getemployeedetail_08")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getemployeedetail_09(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getemployeedetail_09")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getemployeedetail_10(self):
        """缺失token必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getemployeedetail_10")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getemployeedetail_11(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getemployeedetail_11")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getemployeedetail_12(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getemployeedetail_12")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getemployeedetail_13(self):
        """缺失user_id_employee必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getemployeedetail_13")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_14(self):
        """店长邀请已注册的手机号"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_inviteemployee_14")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_15(self):
        """店长邀请已注册的邮箱"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_inviteemployee_15")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_16(self):
        """店长邀请未注册的手机号"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_inviteemployee_16")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_17(self):
        """店长邀请未注册的邮箱"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_inviteemployee_17")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_18(self):
        """店长邀请自己"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_inviteemployee_18")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_19(self):
        """被邀请账号已经加入过该店铺了，不能重复邀请"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_inviteemployee_19")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_20(self):
        """验证码错误"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_inviteemployee_20")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_21(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_inviteemployee_21")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_22(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_inviteemployee_22")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_23(self):
        """缺失username必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_inviteemployee_23")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_24(self):
        """缺失token必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_inviteemployee_24")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_25(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_inviteemployee_25")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_answerinvite_14(self):
        """被邀请者拒绝加入店铺"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_answerinvite_14")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_answerinvite_15(self):
        """在其他设备已拒绝加入店铺"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_answerinvite_15")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_answerinvite_16(self):
        """被邀请者接受加入店铺"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_answerinvite_16")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_answerinvite_17(self):
        """在其他设备已经接受加入店铺了"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_answerinvite_17")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_18(self):
        """店长禁用店员没有填写备注"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_forbiduser_18")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_19(self):
        """店长启用店员"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_forbiduser_19")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_20(self):
        """店长禁用店员填写备注"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_forbiduser_20")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_21(self):
        """店长启用店员"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_forbiduser_21")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_22(self):
        """缺失forbid_remark必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_forbiduser_22")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_23(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_forbiduser_23")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_24(self):
        """缺失status必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_forbiduser_24")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_25(self):
        """缺失token必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_forbiduser_25")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_26(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_forbiduser_26")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_27(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_forbiduser_27")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_28(self):
        """缺失user_id_assign必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_forbiduser_28")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_removeuser_29(self):
        """店长删除店员账号"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_removeuser_29")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_removeuser_30(self):
        """shop_id为70400"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_removeuser_30")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_removeuser_31(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_removeuser_31")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_removeuser_32(self):
        """缺失token必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_removeuser_32")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_removeuser_33(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_removeuser_33")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_removeuser_34(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_removeuser_34")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_removeuser_35(self):
        """缺失user_id_assign必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_removeuser_35")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updatepermission_48(self):
        """店长修改店员权限（店员有权限）"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_updatepermission_48")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updatepermission_49(self):
        """店长修改店员权限（店员没有权限）"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_updatepermission_49")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updatepermission_50(self):
        """店员修改店员的权限"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_updatepermission_50")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updatepermission_51(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_updatepermission_51")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updatepermission_52(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_updatepermission_52")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updatepermission_53(self):
        """缺失permission必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_updatepermission_53")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updatepermission_54(self):
        """缺失user_id_assign必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_updatepermission_54")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updatepermission_55(self):
        """缺失token必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_updatepermission_55")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updatepermission_56(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_updatepermission_56")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_36(self):
        """获取系统消息列表"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getmessage_36")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_37(self):
        """缺失page_num必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getmessage_37")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_38(self):
        """缺失page_size必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getmessage_38")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_39(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getmessage_39")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_40(self):
        """获取消息列表"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getmessage_40")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_41(self):
        """缺失page_num必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getmessage_41")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_42(self):
        """缺失page_size必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getmessage_42")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_43(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getmessage_43")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_44(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"D:\work\test\api_test\api_test\test_file/employee.xlsx",
                                    r"employee",
                                    r"test_getmessage_44")  
        new_data = common.replace_string(case_data[5], 3, case_data[3])
        new_data = new_data.replace('\\', '\\\\')
        new_data = eval(f"f'{new_data}'")  # eval使内层f-string（f''）有效
        # 请求方法get或者post判断
        responses = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data, 
                                           env=3, is_encrypt=True)
        # case相关参数 
        common.show_results(case_data[1], case_data[2], case_data[3], case_data[4], common.resp_result(responses),
                            case_data[6], case_data[7], new_data, 3)  # case_data[5]为原始参数，new_data为实际传入参数
        # 响应结果的断言，保存先判断相应结果不为空，再判断预期与实际结果是否一致
        self.assertFalse(responses is None, "响应结果为空！")  # 如果断言失败，之后的代码不再执行
        self.assertTrue(responses.text[0] == '{' and responses.text[-1] == '}', "响应结果不是json格式！")
        self.assertEqual(common.response_deal(responses.json()[case_data[6]]),
                         common.response_deal(case_data[7]), 
                         "预期与实际结果不一致！")  # 将字符串中所有单引号变成双引号，字符串比较时去除单双引号的影响
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    

if __name__ == "__main__":
    unittest.main() 
