
import unittest
from common import configHttp
from common import common
from common.common import get_response as response
from common.special import mgt_admin_id as mgt
from common.special import partner_admin_id as partner

  
class Backup(unittest.TestCase):  # class_name.title()方法为字符串首字母大写
    """访问量top50的接口"""
    def setUp(self):
        print("\ncase start!\n")

    def tearDown(self):
        print("\ncase end!\n"
              "*****************************************************************************")
        pass
    
    def test_backup_01(self):
        """无店无账号备份正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_backup_01") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_backup_02(self):
        """无店有账号备份正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_backup_02") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_backup_04(self):
        """有店无账号备份正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_backup_04") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_backup_07(self):
        """非法的参数data值"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_backup_07") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_backup_08(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_backup_08") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_backup_09(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_backup_09") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_backup_10(self):
        """缺失data必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_backup_10") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_backup_11(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_backup_11") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_backup_12(self):
        """缺失machine_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_backup_12") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_recover_11(self):
        """非法的备份记录id"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_recover_11") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_recover_12(self):
        """缺失id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_recover_12") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_recover_13(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_recover_13") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_recover_14(self):
        """缺失model必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_recover_14") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_checkMachineToShop_14(self):
        """机器没有绑定到设备"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_checkMachineToShop_14") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_checkMachineToShop_15(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_checkMachineToShop_15") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_checkMachineToShop_16(self):
        """缺失model_detail必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_checkMachineToShop_16") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_machinelist_15(self):
        """正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_machinelist_15") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_machinelist_16(self):
        """sn为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_machinelist_16") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_machinelist_17(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_machinelist_17") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_machinelist_18(self):
        """缺失page_num必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_machinelist_18") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_machinelist_19(self):
        """缺失page_size必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_machinelist_19") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsevenbackuplist_20(self):
        """正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_getsevenbackuplist_20") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsevenbackuplist_21(self):
        """缺失back_sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_getsevenbackuplist_21") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsevenbackuplist_22(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_getsevenbackuplist_22") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_deletebyid_17(self):
        """删除不存在的备份id记录"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"backup",
                                    r"test_deletebyid_17") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
      
class Employee(unittest.TestCase):  # class_name.title()方法为字符串首字母大写
    """大数据接口访问"""
    def setUp(self):
        print("\ncase start!\n")

    def tearDown(self):
        print("\ncase end!\n"
              "*****************************************************************************")
        pass
    
    def test_getsnemployeelist_01(self):
        """获取店铺下的人员列表"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsnemployeelist_02(self):
        """缺失page_num必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsnemployeelist_03(self):
        """缺失page_size必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsnemployeelist_04(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsnemployeelist_05(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsnemployeelist_06(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getsnemployeelist_07(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getemployeedetail_09(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getemployeedetail_10(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getemployeedetail_11(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getemployeedetail_12(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getemployeedetail_13(self):
        """缺失user_id_employee必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_21(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteemployee_22(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_23(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_24(self):
        """缺失status必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_25(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_26(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_27(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_forbiduser_28(self):
        """缺失user_id_assign必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_removeuser_30(self):
        """shop_id为70400"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_removeuser_31(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_removeuser_32(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_removeuser_33(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_removeuser_34(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_removeuser_35(self):
        """缺失user_id_assign必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updatepermission_53(self):
        """缺失permission必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_36(self):
        """获取系统消息列表"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_37(self):
        """缺失page_num必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_38(self):
        """缺失page_size必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_39(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_40(self):
        """获取消息列表"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_41(self):
        """缺失page_num必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_42(self):
        """缺失page_size必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_43(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getmessage_44(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
      
class Machine(unittest.TestCase):  # class_name.title()方法为字符串首字母大写
    """"""
    def setUp(self):
        print("\ncase start!\n")

    def tearDown(self):
        print("\ncase end!\n"
              "*****************************************************************************")
        pass
    
    def test_getShopMachineList_01(self):
        """正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_getShopMachineList_01") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getShopMachineList_02(self):
        """sn为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_getShopMachineList_02") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getShopMachineList_03(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_getShopMachineList_03") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getShopMachineList_04(self):
        """缺失page_num必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_getShopMachineList_04") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getShopMachineList_05(self):
        """缺失page_size必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_getShopMachineList_05") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchMachine_07(self):
        """sn不存在"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_searchMachine_07") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchMachine_12(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_searchMachine_12") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchMachine_13(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_searchMachine_13") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchMachine_14(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_searchMachine_14") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchMachine_15(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_searchMachine_15") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteMachine_16(self):
        """正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_inviteMachine_16") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteMachine_17(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_inviteMachine_17") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteMachine_18(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_inviteMachine_18") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteMachine_19(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_inviteMachine_19") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteMachine_20(self):
        """缺失sn_assign必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_inviteMachine_20") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteMachine_21(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_inviteMachine_21") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_inviteMachine_22(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_inviteMachine_22") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_unBindMachine_24(self):
        """店员没有解绑权限"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_unBindMachine_24") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_unBindMachine_25(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_unBindMachine_25") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_unBindMachine_26(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_unBindMachine_26") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_unBindMachine_27(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_unBindMachine_27") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_unBindMachine_28(self):
        """缺失sn_assign必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_unBindMachine_28") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_unBindMachine_29(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_unBindMachine_29") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_unBindMachine_30(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_unBindMachine_30") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getBaseInfo_1(self):
        """正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_getBaseInfo_1") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getBaseInfo_2(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_getBaseInfo_2") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getListBy_3(self):
        """正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_getListBy_3") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getListBy_4(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_getListBy_4") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getMachineImg_5(self):
        """正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_getMachineImg_5") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getMachineImg_6(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"machine",
                                    r"test_getMachineImg_6") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
      
class Sendmsgtomachine(unittest.TestCase):  # class_name.title()方法为字符串首字母大写
    """"""
    def setUp(self):
        print("\ncase start!\n")

    def tearDown(self):
        print("\ncase end!\n"
              "*****************************************************************************")
        pass
    
    def test_sendMsgToMachine_01(self):
        """消息跳转类型为app_消息操作类型为type 1（纯文本消息）_发送范围为range 1（消息）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_01") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_02(self):
        """消息跳转类型为app_消息操作类型为type 0（可操作的消息）_发送范围为range 1（消息）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_02") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_03(self):
        """消息跳转类型为app_消息操作类型为type 1（纯文本消息）_发送范围为range 2（推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_03") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_04(self):
        """消息跳转类型为app_消息操作类型为type 0（可操作的消息）_发送范围为range 2（推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_04") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_05(self):
        """消息跳转类型为app_消息操作类型为type 1（可操作的消息）_发送范围为range 0（消息&推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_05") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_06(self):
        """消息跳转类型为app_消息操作类型为type 0（可操作的消息）_发送范围为range 0（消息&推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_06") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_07(self):
        """消息跳转类型为H5_消息操作类型为type 1（纯文本消息）_发送范围为range 1（消息）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_07") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_08(self):
        """消息跳转类型为H5_消息操作类型为type 0（可操作的消息）_发送范围为range 1（消息）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_08") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_09(self):
        """消息跳转类型为H5_消息操作类型为type 1（纯文本消息）_发送范围为range 2（推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_09") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_10(self):
        """消息跳转类型为H5_消息操作类型为type 0（可操作的消息）_发送范围为range 2（推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_10") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_11(self):
        """消息跳转类型为H5_消息操作类型为type 1（可操作的消息）_发送范围为range 0（消息&推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_11") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_12(self):
        """消息跳转类型为H5_消息操作类型为type 0（可操作的消息）_发送范围为range 0（消息&推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_12") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_13(self):
        """消息跳转类型为text_消息操作类型为type 1（纯文本消息）_发送范围为range 1（消息）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_13") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_14(self):
        """消息跳转类型为text_消息操作类型为type 0（可操作的消息）_发送范围为range 1（消息）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_14") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_15(self):
        """消息跳转类型为text_消息操作类型为type 1（纯文本消息）_发送范围为range 2（推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_15") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_16(self):
        """消息跳转类型为text_消息操作类型为type 0（可操作的消息）_发送范围为range 2（推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_16") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_17(self):
        """消息跳转类型为text_消息操作类型为type 1（可操作的消息）_发送范围为range 0（消息&推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_17") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_18(self):
        """消息跳转类型为text_消息操作类型为type 0（可操作的消息）_发送范围为range 0（消息&推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_18") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_19(self):
        """消息跳转类型为module_消息操作类型为type 1（纯文本消息）_发送范围为range 1（消息）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_19") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_20(self):
        """消息跳转类型为module_消息操作类型为type 0（可操作的消息）_发送范围为range 1（消息）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_20") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_21(self):
        """消息跳转类型为module_消息操作类型为type 1（纯文本消息）_发送范围为range 2（推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_21") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_22(self):
        """消息跳转类型为module_消息操作类型为type 0（可操作的消息）_发送范围为range 2（推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_22") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_23(self):
        """消息跳转类型为module_消息操作类型为type 1（可操作的消息）_发送范围为range 0（消息&推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_23") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_24(self):
        """消息跳转类型为module_消息操作类型为type 0（可操作的消息）_发送范围为range 0（消息&推送）"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_24") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_25(self):
        """传一个sn参数"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_25") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_26(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_26") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_27(self):
        """缺失sender_name必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_27") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_28(self):
        """缺失content必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_28") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_29(self):
        """缺失type必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_29") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_30(self):
        """缺失msg_key必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_30") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_31(self):
        """缺失msg_value必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_31") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_32(self):
        """缺失range必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_32") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_33(self):
        """sn为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_33") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_34(self):
        """sender_name为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_34") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_35(self):
        """content为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_35") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_36(self):
        """type为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_36") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_37(self):
        """msg_key为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_37") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_38(self):
        """msg_value为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_38") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_sendMsgToMachine_39(self):
        """range为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"sendmsgtomachine",
                                    r"test_sendMsgToMachine_39") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
      
class Shop(unittest.TestCase):  # class_name.title()方法为字符串首字母大写
    """"""
    def setUp(self):
        print("\ncase start!\n")

    def tearDown(self):
        print("\ncase end!\n"
              "*****************************************************************************")
        pass
    
    def test_createShop_01(self):
        """创建门店成功"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_createShop_01") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_createShop_02(self):
        """user_id为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_createShop_02") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_createShop_03(self):
        """shop_name为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_createShop_03") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_createShop_04(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_createShop_04") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_createShop_05(self):
        """缺失shop_name必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_createShop_05") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_createShop_06(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_createShop_06") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_createShop_07(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_createShop_07") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_viewShop_36(self):
        """正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_viewShop_36") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_viewShop_37(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_viewShop_37") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchshop_1(self):
        """手机号搜索门店成功"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_searchshop_1") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchshop_3(self):
        """username邮箱不存在"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_searchshop_3") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchshop_4(self):
        """username手机号不存在"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_searchshop_4") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchshop_5(self):
        """username为特殊字符"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_searchshop_5") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchshop_6(self):
        """username为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_searchshop_6") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchshop_7(self):
        """缺失username必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_searchshop_7") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchshop_8(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_searchshop_8") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchshop_9(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_searchshop_9") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_searchshop_10(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_searchshop_10") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_applyJoinShop_11(self):
        """正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_applyJoinShop_11") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_applyJoinShop_12(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_applyJoinShop_12") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_applyJoinShop_13(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_applyJoinShop_13") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_applyJoinShop_14(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_applyJoinShop_14") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_applyJoinShop_15(self):
        """缺失user_id_assign必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_applyJoinShop_15") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_applyJoinShop_16(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_applyJoinShop_16") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_applyJoinShop_17(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_applyJoinShop_17") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_reply_29(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_reply_29") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_reply_30(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_reply_30") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_reply_31(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_reply_31") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_reply_32(self):
        """缺失user_id_assign必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_reply_32") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_reply_33(self):
        """缺失status必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_reply_33") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_reply_34(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_reply_34") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_reply_35(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_reply_35") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_reply_36(self):
        """缺失uniqid必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_reply_36") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getUserInfo_18(self):
        """正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_getUserInfo_18") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getUserInfo_19(self):
        """缺失user_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_getUserInfo_19") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getUserInfo_20(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_getUserInfo_20") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getUserInfo_21(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_getUserInfo_21") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_setMachineIsFind_22(self):
        """设备功能被发现0关闭"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_setMachineIsFind_22") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_setMachineIsFind_23(self):
        """设备功能被发现1打开"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_setMachineIsFind_23") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_setMachineIsFind_24(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_setMachineIsFind_24") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_setMachineIsFind_25(self):
        """缺失status必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_setMachineIsFind_25") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_checkusername_26(self):
        """username为手机号正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_checkusername_26") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_checkusername_27(self):
        """username为邮箱正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_checkusername_27") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_checkusername_28(self):
        """缺失username必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_checkusername_28") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_dashboradShopInfo_30(self):
        """正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_dashboradShopInfo_30") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_dashboradShopInfo_31(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_dashboradShopInfo_31") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_dashboradBackup_33(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_dashboradBackup_33") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getListByBatch_34(self):
        """正常数据校验"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_getListByBatch_34") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getListByBatch_35(self):
        """缺失sn必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_getListByBatch_35") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShop_38(self):
        """修改门店名称成功"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShop_38") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShop_39(self):
        """修改联系人成功"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShop_39") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShop_40(self):
        """修改联系电话成功"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShop_40") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShop_41(self):
        """修改门店地址成功"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShop_41") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShop_42(self):
        """修改营业时间成功"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShop_42") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShop_43(self):
        """缺失key必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShop_43") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShop_44(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShop_44") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShop_45(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShop_45") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShop_46(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShop_46") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShop_47(self):
        """缺失value必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShop_47") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShop_48(self):
        """shop_id为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShop_48") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_getShopTYpeList_49(self):
        """获取经营品类列表信息成功"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_getShopTYpeList_49") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShopType_50(self):
        """修改经营品类成功"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShopType_50") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShopType_51(self):
        """缺失shop_id必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShopType_51") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShopType_52(self):
        """缺失token必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShopType_52") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShopType_53(self):
        """缺失token_shop必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShopType_53") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShopType_54(self):
        """缺失type_one必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShopType_54") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShopType_55(self):
        """缺失type_one_name必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShopType_55") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShopType_56(self):
        """缺失type_two必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShopType_56") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShopType_57(self):
        """缺失type_two_name必传项"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShopType_57") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    
    def test_updateShopType_58(self):
        """shop_id为空"""
        case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_shanghu\test_file/SunmiUsercenter.xlsx",
                                    r"shop",
                                    r"test_updateShopType_58") 
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
                         "预期与实际结果不一致！")
        # 输出结果
        print("接口响应结果与预期一致，测试通过！")        
    

if __name__ == "__main__":
    unittest.main() 
