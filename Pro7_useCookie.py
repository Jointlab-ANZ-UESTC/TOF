import requests
import csv
 # Support cookie

def useCookie(cookie_file,url_file,html_file):
    f = open(cookie_file, 'r') # 打开存放cookie内容的文件
    u = open(url_file,'r') # 打开存放url的文件
    h = open(html_file,'w',encoding='utf-8') # 存放所得到的网页内容的文件
    reader = csv.reader(u)
    urls = [x for x in reader] # 每个元素都是一个list
    for url in urls:
        url = url[0]
    cookies = {} # 初始化cookies字典变量
    for line in f.read().split(';'): # 按照字符‘;’进行划分读取
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    res = requests.get(url, cookies=cookies) # 使用cookies向网页请求内容
    h.write(res.text)
    f.close()
    u.close()
    h.close()


if __name__=='__main__':
  useCookie('Proj7_cookie.txt','Proj7_url.csv','Proj7_response.html')
