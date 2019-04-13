import requests
import csv
import time
from pandas import Series,DataFrame
import pandas as pd
#Check 200+ html

with open('test.csv')as f:
    reader=csv.reader(f)
    urls=[x for x in reader]#每个元素都是一个list
    final_url=[]#记录读取的url
    final_code=[]#记录URL对应的状态码
    for url in urls:
        url=url[0]
        res=requests.get(url)#得到URL状态
        status_code=res.status_code
        print(url,status_code)
        final_url.append(url)#向队列中添加url
        final_code.append(status_code)#向队列中添加状态码

def converttoHtml(url, status_code):
    data={"url":url,"marks":status_code}#dict：url：状态码
    df=DataFrame(data)#利用dict生成DataFrame对象
    h = df.to_html('F:\\github project\\PROJ-3\\test.html')#写入HTML文件中
    return h

converttoHtml(final_url,final_code)
f.close()