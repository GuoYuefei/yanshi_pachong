#!/usr/bin/python
# coding:utf8
import sys, urllib, urllib2
import pytesseract
from PIL import Image
import cookielib

#这时候我们发现这个可以通过get方式登录（自己抓包分析）
# 该类掌管登录盐城师范学院的学生管理系统的功能
class Login:
    reload(sys)
    sys.setdefaultencoding('utf8')
    #构造函数需要传入帐号与密码
    def __init__(self,username='14163119',password='32020119960723304X'):
        self.username = username
        self.password = password
        #用于记录循环几次才登录成功的循环因子
        self.i = 0
        #这个json形式的字符串用于记录登录信息，提供给外部用于判断是否模拟登录成功
        self.login_info = '{"result":0,"msg":""}'
        self.headers = {
            'Host':'sms.yctu.edu.cn',
            'Referer': 'http: // sms.yctu.edu.cn / home / index',
            'User - Agent':'Mozilla/5.0(X11;Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        # 要提交登录表单的地方
        self.LOGIN_HOST = "http://sms.yctu.edu.cn/home/loginHandle"
        # 验证码地址，用于获取验证码
        self.code_host = 'http://sms.yctu.edu.cn/home/verify'
        # 这个变量暂时貌似没什么用处
        self.HOME_HOST = "http://sms.yctu.edu.cn/student/profile"
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    #向外提供改变密码的set函数
    def set_password(self,password):
        self.password = password

    #将网络上的图片文件保存到本地，并且返回值为图片所在的地址
    def get_codeImage(self,address='code'):
        # 把图片暂时存在这个地址
        image_address = address
        image_req = urllib2.Request(self.code_host)
        response = self.opener.open(image_req)
        f = file(image_address, 'w+')
        f.write(response.read())
        f.flush()
        # 这里返回该图片所在地址
        return image_address

    # 获取成功
    # get_codeImage(code_host)

    #传入图片地址就可以orc出图片信息，返回识别出的文本
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

    #这是进行登录部分的函数,返回登录后的页面的文本文档
    def logining(self,code_string):
        #data = {'username': '14163119', 'password': '32020119960723304X', 'verify': code_string}
        #对需要发送的数据进行编码
        #login_data = urllib.urlencode(data)
        #login_req = urllib2.Request(self.LOGIN_HOST+'?logindata=username=14163119&password=32020119960723304X&verify='+code_string,headers=self.headers)
        #该登录方式是隐式的get方式
        login_data = {}
        login_data['login_data'] = 'username=+'+self.username+'&password='+self.password+'&verify='+code_string
        get_data = urllib.urlencode(login_data)
        print get_data
        login_response = self.opener.open(self.LOGIN_HOST+'?'+get_data)
        #把登录的相关信息记录起来,可以通过该变量来判断登录情况  {"result":0,"msg":"\u8868\u5355\u6570\u636e\u586b\u5199\u9519\u8bef"}
        self.login_info = login_response.read()
        home_response = self.opener.open(self.HOME_HOST)
        #print home_response.read()
        #返回登录后的页面
        return home_response

# data = {'username': '14163119', 'password': '32020119960723304X', 'verify': code_string}

import json
# 用于测试这个类
if __name__ == '__main__':
    login = Login()
    while True:
        login.i += 1
        path = login.get_codeImage()
        code_string = login.code_to_string(path)

        #code_string = raw_input("please input code: ")
        result=login.logining(code_string).read()
        #print login.login_info
        #if login.login_info == ‘
        #json.loads()可以将一个json形式的字符串转化成一个字典
        info_json = json.loads(login.login_info)
        print login.login_info

        #print info_json['result']
        print code_string
        if login.i%10 == 0:
            print '-----------------------------' +str(login.i) + \
                  '------------------------------------'
        print info_json['msg']
        #判断登录是否成功，成功就跳出
        if info_json['result'] == 1:
            break
    print result
    #输出尝试次数
    print login.i


