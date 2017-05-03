#!/usr/bin/python
# coding:utf8

#from yanshixinxipachong import test1


class InfoHandle():
    def __init__(self):
        pass

    def parseUsername(self):
        pass

    #主要是对身份证号的18位数据进行分析，只有最后一位会出现字母x其他都为正常数字
    '''首先分析他们学校的初始密码是身份证号，
        1-2.而且大多是江苏人，也就是大多是以32开头
        3-4.江苏一共13个地级市，这两位必定是从01到13
        5-6,这个是区县位，江苏最多区县的是南京13个，所以这个数字的上限是13，故是01-13
        7-14,这个是生日位。先爬14界。大多是95或者96年。所以可以从19950101-19961231
        15-16,这个是所在派出所的编号位00-99
        17,性别位，男奇女偶
        18,是个人校验位。为计算机自动生成，存在字母x
        如果电脑每分钟尝试200次，破解一个密码需要12年
    '''
    def parsePassword(self):

        pass

    #连接字符串
    def __dataCon(self,source,Destination):
        return source+Destination

    def __dataHandle(self,start=0,end=1000,step=2):
        #总是三位数输出,其中end不包括
        #因为爬取的是女生的信息，所以步进为2,最后第二位身份证是偶数的是女生
        for x in xrange(start,end,step):
            if x>=100:
                yield str(x)
            elif 10<=x<100:
                yield '0'+str(x)
            else:
                yield '00'+str(x)
        #结束了就输出-1提醒
        yield -1

    #针对身份证最后可能出现x进行处理
    def __dataLastHandle(self):
        tuple1 = (0,1,2,3,4,5,6,7,8,9,'X')
        for x in tuple1:
            yield str(x)
        yield -1

    #函数测试成功，后四位封装完毕
    def dataLast4(self,start=0,end=1000,step=2):
        #三个字母变量代表后4到后1
        #一个字母变量代表最后一位
        xyz = self.__dataHandle(start,end,step)
        z = self.__dataLastHandle()
        while True:
            abc = xyz.next()
            #取完为止，跳出循环
            if abc == -1:
                break
            while True:
                a = z.next()
                #取完为止，跳出循环
                if a== -1:
                    #这一步是为了重新开始计数
                    z = self.__dataLastHandle( )
                    break
                yield  self.__dataCon(abc,a)
        #取完之后依旧返回-1提醒
        yield -1


if __name__=='__main__':
    info = InfoHandle()
   #r = info.dataHandle(0,2)
   #print r.next()
   #print r.next()
   #print r.next()
#   x = info.dataHandle()
    passwd = info.dataLast4()
    x = passwd.next()
    while x != -1:
        print x
        x = passwd.next()