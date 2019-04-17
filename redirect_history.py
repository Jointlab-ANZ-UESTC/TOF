import requests

try:
    f_url = open('proj4_url.csv', 'r')  # 打开含有url的文件
    f2_result=open('proj4_result.csv','w+')  # 打开保存查询结果的CSV文件
    f_html=open('proj4_result.html','w+')  # 打开保存查询结果的HTML文件

    url_list = f_url.readlines()  # 读取文件内容，将文件中每一行作为list的一项插入list中。
    print("<html>\
            <head>redirect history</head>\
          <body>", file=f_html)  # 将HTML头部先写入HTML文件中。
    for url in url_list:  # 遍历每行的url文件
        response = requests.get(url)  # 获取每一行的url内容并且调用requests.get方法将调用url相关的内容储存在response变量中。
        if response.history:  # 如果response.history有内容，则说明有重定向发生了。
            print("<p>Request was redirected</p>", file=f_html)
            print("Request was redirected", file=f2_result)
            for resp in response.history:   # 重定向的历史
                print('<p>'+resp.url + '->'+'</p>', file=f_html)
                print(resp.url+'->', file=f2_result)
            print('<p>'+response.url+'</p>'+'&nbsp', file=f_html)
            print(response.url+'\n', file=f2_result)   # 最终的地址
        else:  # 没有重定向发生，输出没有重定向即可。
            print('<p>'+url+'</p>', file=f_html)
            print("<p>Request was not redirected</p>\n", file=f_html)
            print(url,file=f2_result)
            print("Request was not redirected\n", file=f2_result)
    print('''</body>
            </html>''',file=f_html)  # 在末尾将HTML的尾部补全。
finally:
    if f_url:
        f_url.close()  # 确保文件被关闭
    if f2_result:
        f2_result.close()
    if f_html:
        f_html.close()

