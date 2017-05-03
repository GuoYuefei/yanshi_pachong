#!/usr/bin/python
# coding:utf8
import sys, urllib, urllib2
import pytesseract
from PIL import Image
import cookielib


# 该类掌管登录盐城师范学院的学生管理系统的功能
class Login:
    reload(sys)
    sys.setdefaultencoding('utf8')

    def __init__(self):
        self.headers = {
            'Host':'sms.yctu.edu.cn',
            'Referer': 'http: // sms.yctu.edu.cn / home / index',
            'User - Agent':'Mozilla/5.0(X11;Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        # 要提交登录表单的地方
        self.LOGIN_HOST = "http://sms.yctu.edu.cn/home/login"
        # 验证码地址，用于获取验证码
        self.code_host = 'http://sms.yctu.edu.cn/home/verify'
        # 这个变量暂时貌似没什么用处
        self.HOME_HOST = "http://sms.yctu.edu.cn/student/profile"
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def get_codeImage(self):
        # 把图片暂时存在这个地址
        image_address = 'code'
        image_req = urllib2.Request(self.code_host)
        response = self.opener.open(image_req)
        f = file(image_address, 'w+')
        f.write(response.read())
        f.flush()
        # 这里返回该图片所在地址
        return image_address

    # 获取成功
    # get_codeImage(code_host)

    def code_to_string(self, image_address):
        image = Image.open(image_address)
        code_string = pytesseract.image_to_string(image)
        return code_string

        # 识别成功
        # print code_to_string('code')

        # 以上两个函数的测试
        # 经过测试50次只有5次成功，成功概率暂时定为10%
        # path = get_codeImage(code_host)
        # print code_to_string(path)
    #这是进行登录部分的函数
    def logining(self,code_string):
        data = {'username': '14163119', 'password': '32020119960723304X', 'verify': code_string}
        #对需要发送的数据进行编码
        login_data = urllib.urlencode(data)
        login_req = urllib2.Request(self.LOGIN_HOST, login_data, self.headers)
        login_response = self.opener.open(login_req)
        #print login_response.read()
        home_response = self.opener.open(self.HOME_HOST)
        print home_response.read()

# data = {'username': '14163119', 'password': '32020119960723304X', 'verify': code_string}

# 用于测试这个类
if __name__ == '__main__':
    login = Login()
    path = login.get_codeImage()
    code_string = login.code_to_string(path)

    img_code = raw_input("please input code: ")
    login.logining(img_code)
    print code_string
