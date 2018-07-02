# -*- coding:utf-8 -*-
import requests
from lxml import etree
import sys
import codecs

import importlib
importlib.reload(sys)

def getfromBaidu(word):
    list=[]
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
        }
    baiduurl = 'http://www.baidu.com'
    url = 'http://www.baidu.com.cn/s?wd=' + word + '&cl=3'
    html = requests.get(url=url,headers=headers)
    path = etree.HTML(html.content)
    #用k来控制爬取的页码范围

    for k in range(1, 5):
        path = etree.HTML(requests.get(url, headers).content)
        flag = 11
        if k == 1:
            flag = 10

        for i in range(1, flag):
            sentence = ""
            for j in path.xpath('//*[@id="%d"]/h3/a//text()'%((k-1)*10+i)):
                sentence+=j
            #print(sentence.encode('utf-8'))
            #print(sentence)
            list.append(sentence.encode('utf-8'))
        url = baiduurl+path.xpath('//*[@id="page"]/a[%d]/@href'%flag)[0]
    return list

#主程序测试函数
if __name__ == '__main__':
    #读取参数：关键词
    word = '胖子哥'
    if len(sys.argv) == 2:
        word = sys.argv[1]
    else:
        print(sys.argv)
    print(sys.argv)
    #执行查询
    out = getfromBaidu(word)
    #print(out)

    for i in range(1,len(out)):
        str = bytes.decode(out[i])
        print(str)
