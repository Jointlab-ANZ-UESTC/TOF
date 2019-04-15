import requests

try:
    f_url = open('url.csv', 'r')  # 打开含有url的文件
    f2_result=open('result.csv','w+')  # 打开保存查询结果的CSV文件
    f_html=open('result.html','w+')  # 打开保存查询结果的HTML文件

    url_list = f_url.readlines()  # 读取文件内容
    print("<html>\
            <head>redirect history</head>\
          <body>", file=f_html)
    for url in url_list:  # 遍历每行的url文件
        response = requests.get(url)
        if response.history:
            print("<p>Request was redirected</p>", file=f_html)
            print("Request was redirected", file=f2_result)
            for resp in response.history:   # 重定向的历史
                print('<p>'+resp.url + '->'+'</p>', file=f_html)
                print(resp.url+'->', file=f2_result)
            print('<p>'+response.url+'</p>'+'&nbsp', file=f_html)
            print(response.url+'\n', file=f2_result)   # 最终的地址
        else:
            print('<p>'+url+'</p>', file=f_html)
            print("<p>Request was not redirected</p>\n", file=f_html)
            print(url,file=f2_result)
            print("Request was not redirected\n", file=f2_result)
    print('''</body>
            </html>''',file=f_html)
finally:
    if f_url:
        f_url.close()  # 确保文件被关闭
    if f2_result:
        f2_result.close()
    if f_html:
        f_html.close()

