# coding=utf-8
import urllib2
import urllib
import re
import sys
import os


# coding:utf-8


def get_bing_backimg():
    print(os.getcwd())
    if os.path.exists(os.getcwd()+'/photos') == True:  # 如果目录不存在则创建
        print("photo dir is exsit")
    else:
        os.mkdir('photos')

    for i in range(0, 39):
        url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=' + str(i) + '&n=1&nc=1361089515117&FORM=HYLH1'
        content = urllib.urlopen(url).read()  # 获取网页王源
        if content == 'null':
            print ('open & read bing error')
            # sys.exit(-1)
        content = content.decode('utf-8')
        reg = re.compile('"url":"(.*?)","urlbase"', re.S)
        text = re.findall(reg, content)  # 正则获取图片的URL
        print (text)
        for imgurl in text:  # 遍历下载所有的图片
            right = imgurl.rindex('/')
            name = imgurl.replace(imgurl[:right + 1], '')
            savepath = 'photos/' + name
            if os.path.exists(os.getcwd()+'/'+savepath):
                print(name + ' is exist')
            else:
                urllib.urlretrieve('http://cn.bing.com' + imgurl, savepath)  # 下载图片
            print (name + ' save success')

    print (content)


# get_bing_backimg()
