

# from common import common
# remote = '2018-08-01 23_58_43result.html'
# common.upload_file(remote)

# path = r"C:\Users\Administrator\PycharmProjects\api_test\result\20180803_161647-result.html"
# rer = open(path,'rb').read()
# if u"商米" in rer:
#     print("gyee")


# from PIL import Image
# im = Image.open(r"C:\Users\Administrator\PycharmProjects\api_test\result\20181105_235843-summary.html")
#
# print(im.format, im.size, im.mode)
# im.save(r'c.jpg')

###########################################################################################################
"""邮件发送，将html中图片的发送出去，使用base64编码方式将图片代码放到html文件中"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64

sender = 'qa@sunmi.com'
receiver = 'guhaitao@sunmi.com'  # guhaitao@sunmi.com,zhanggaoxian@sunmi.com,
subject = 'python email test'
smtp_server = 'smtp.exmail.qq.com'
username = 'qa@sunmi.com'
password = 'sUNMI388'

mail_context = MIMEMultipart('related')
mail_context['Subject'] = 'test message'


co = open(r'C:\Users\Administrator\Desktop\te.png', 'rb').read()
base64_data = base64.b64encode(co)
print(base64_data)
base64_data = str(base64_data)[2:-1]
print(base64_data, '\n', type(base64_data))

# context = MIMEText('<html><body><img src="cid:img1" alt="图片文字说明" width=200 height=100/></body></html>',
#                    'html', 'utf-8')

content = f'<html><body><img src="data:image/jpg;base64,{base64_data}"/></body></html>'
context = MIMEText(content, 'html', 'utf-8')
mail_context.attach(context)

smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(username, password)
smtp.sendmail(sender, receiver, mail_context.as_string())
print('成功！')
smtp.quit()


#############################################################################################################


from common import common
import json
from common import configHttp
from common import encrypt
from common.common import get_response as response


excel = r'C:\Users\Administrator\PycharmProjects\api_test\test_file\bigdat.xlsx'
sheet = 'sub'
case = 'test_01_DataSub_store'
lis = common.get_case(excel, sheet, case)
js = json.dumps(lis[5])
print(lis, '\n', type(lis[5]), '\n', lis[5], '\n', js, '\n', json.loads(js), '\n', eval(js))





from common import configHttp
from common import common
from common.common import get_response as response
from common.special import mgt_admin_id as mgt

id = mgt('guhaitao@sunmi.com', 'qwer1234')
print(id)

case_data = common.get_case(r"C:\Users\Administrator\PycharmProjects\api_test\test_file/bigdat.xlsx",
                            r"ds",
                            r"test_01_Dsupload_update")


data = common.replace_string(case_data[5])
print(data, type(data))

new_data = eval(f"f'{data}'")
new_data = common.replace_str(new_data)
print(new_data, type(new_data))

response = configHttp.post_or_get(case_data[2], case_data[3], case_data[4], new_data)
print(response.json(), type(response.json()), response.text)





from common import common
from common.common import get_response as response
a = r"bigdat.xlsx"
b = r"data"
c = r"test_01_gerserverstatus"


# rio = response(a, b, c, 1, True, 'code')
# print(rio)

na = '{"dataService":null,"dsVersion":response(a, b, c, 1, True, \"code\"),"machineModel":"V1","msn":"V10216BM01932"}'
data = common.replace_string(na)
print(data, type(data))
new_data = eval(f"f'{data}'")
print(new_data, type(new_data))


from common import configHttp
from common import encrypt

password = encrypt.encrypt_long('qwer1234')['params']
ress = configHttp.post_or_get('post',
                              r'http://uat.webapi.sunmi.com/webapi/sunmisso/web/sunmisso/1.0/',
                              r'service=OAuth.authorizeLogin',
                              f'{{"clientId":"sm5bee3f7394136","userName":"guhaitao@sunmi.com","password":"{password}","type":"1"}}',
                              1,
                              True)
print(ress.json())
jss = ress.json()['data']['code']
print(jss)

pp = ("data", 5, "appName")

for i in pp:
    jss = jss[i]

print(jss)

print(jss,'\n', type(jss), '\n', type(jss['data'][1]))

pre = {'re':[{'test':98},{'lo':0}]}

def ger(ab, *args):
    print(ab, args)
    for i in args:
        ab = ab[i]
        print(i,type(i),ab)
ger({'re':[{'test':98},{'lo':0}]}, 're',0 ,'test')


from common import common
from common import configHttp
qa = {"dataService":{"com.sunmi.dataService":[{"dataName":"bluetooth_info","sData":"[{\"deviceClass\":0,\"deviceName\":\"InnerPrinter\",\"macAddress\":\"00:11:22:33:44:55\",\"time\":1534784327},{\"deviceClass\":524,\"deviceName\":\"V2\",\"macAddress\":\"B4:3A:F0:06:14:D1\",\"time\":1534784327},{\"deviceClass\":524,\"deviceName\":\"yunjing\",\"macAddress\":\"44:00:10:72:93:D0\",\"time\":1534784327}]","sTime":1534813127}]},"dsVersion":"3.1.3","machineModel":"V1","msn":"V10216BM01932"}
data = common.replace_string(qa)
new_data = eval(f"f'{data}'")

from common.special import mgt_admin_id as mgt
print(mgt('admin', 'admin'))


#=======================================================================================================


from common import configHttp
ress = configHttp.post_or_get('get',
                              r'http://apiwire:123456@47.98.173.56:8080/jenkins/job/Tyrants/buildWithParameters',
                              r'token=triggertyrant&option=set&username=lvbu@sunmi.com&password=15262517121Lvbu&machine_model=V1&package_name_list=com.sohu.inputmethod.sogou')
print(ress.text)


from common import configHttp
from common import encrypt


password = encrypt.encrypt_long('gu123456')['params']
ress = configHttp.post_or_get('post',
                              r'http://uat.webapi.sunmi.com/webapi/partners/web/developers/1.2/',
                              r'service=PartnerUser.login',
                              f'{{"userName":"gu001","passWord":"{password}"}}',
                              1,
                              True)

print(type(ress.json()['code']))

#=========================================================================================================


from datetime import datetime
import xlrd
# filename, sheetname = decode(filename, sheetname)
# rbook = xlrd.open_workbook(filename)
# sheet = rbook.sheet_by_name(sheetname)
cls = []
file = xlrd.open_workbook(r'C:\Users\Administrator\PycharmProjects\api_test\test_file\接口列表.xlsx')
# get sheet by name
sheet_page = file.sheet_by_name('top10')
# get one sheet's rows
num_rows = sheet_page.nrows
ce = sheet_page.cell_value(60, 7)

print('【'+str(ce)+'】', type(ce))

for i in range(num_rows):
    if sheet_page.row_values(i)[0] == 'test_01_datacollectrom_info':
        len_list = len(sheet_page.row_values(i))
        for j in range(len_list):
            cell_type = sheet_page.cell(i, j).ctype  # c_type： 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
            cell = sheet_page.cell_value(i, j)
            if cell_type == 1:  # 去掉字符串两边的空格
                n = m = 0
                for x in range(len(cell)):
                    if cell[x] == ' ' and x == n:
                        n += 1
                    if cell[-(x+1)] == ' ' and x == m:
                        m += 1
                if m == 0:
                    cell = cell[n:]
                else:
                    cell = cell[n:-m]
            elif cell_type == 2 and cell % 1 == 0:  # 如果是整型数据
                cell = cell
            elif cell_type == 3:  # 日期类型数据
                year, month, day, hour, minute, second = xlrd.xldate_as_tuple(cell, 0)  # 元组(2015, 12, 10, 17, 47, 34)
                date = datetime(year, month, day, hour, minute, second)
                cell = date.strftime('%Y-%d-%m %H:%M:%S')
            elif cell_type == 4:  # 布尔型数据
                cell = True if cell == 1 else False
            cls.append(cell)
print(cls)



from common import common

a = 1
b = '1'
c = 2.0000
d = '-9.'

e = [a, b, c, d]
for i in e:
    print(common.response_deal(i))

