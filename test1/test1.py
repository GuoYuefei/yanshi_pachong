#!/usr/bin/python
# coding:utf8
import sys,urllib,urllib2
import pytesseract
from PIL import Image
reload(sys)
sys.setdefaultencoding('utf8')

#要提交登录表单的地方
LOGIN_HOST = "http://sms.yctu.edu.cn/home/login"
#验证码地址，用于获取验证码
code_host = 'http://sms.yctu.edu.cn/home/verify'
#这个变量暂时貌似没什么用处
HOME_HOST = "http://222.188.0.102/loginAction.do"

def get_codeImage(code_host):
    image_address = 'code'
    response = urllib.urlopen(code_host)
    f = file(image_address,'w+')
    f.write(response.read())
    #这里返回该图片所在地址
    return image_address
#获取成功
#get_codeImage(code_host)

def code_to_string(image_address):
    image = Image.open(image_address)
    code_string = pytesseract.image_to_string(image)
    return code_string
#识别成功
#print code_to_string('code')

#以上两个函数的测试
#经过测试50次只有5次成功，成功概率暂时定为10%
#path = get_codeImage(code_host)
#print code_to_string(path)

#帐号密码外加验证码
path = get_codeImage(code_host)
code_string = code_to_string(path)

data = {'username': '14163119', 'password': '32020119960723304X','verify':code_string}




data = urllib.urlencode(data)
request = urllib2.Request(LOGIN_HOST)

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor)
response = opener.open(LOGIN_HOST,data,20)
result = response.read()

print str(result)
print code_string
