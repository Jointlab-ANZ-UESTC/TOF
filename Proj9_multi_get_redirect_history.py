import multiprocessing
import requests
import csv
import time


def write_csv(written_file, content):
        """
        写csv文件的函数
        :param written_file: string,被写文件路径名
        :param content: list，被写内容
        :return: void
        """
        with open(written_file, "a", newline="") as f:
            # newline=""为的是使被写文件两行之间不出现空行
           f.write(content)



def read_csv(read_file):
    """
    读csv文件的函数
    :param read_file: string,被读文件路径名
    :return: list,被读出的内容
    """
    with open(read_file, "r") as f:
        reader = csv.reader(f)
        content = list(reader)
        return content


def write_html(html_written_file,content):
    """
        写入html文件的函数
        :param html_written_file:  string 被写文件路径名
        :param content: string,被写的内容
        :return: void
    """
    with open(html_written_file, "a", newline="",encoding="utf-8") as f:
        # newline=""为的是使被写文件两行之间不出现空行
        # encoding="utf_8"是为了避免乱码问题
        f.write(content)


def get_redirect_history(url,result_csv_file,result_html_file):
    """
    :param url: string,存放url
    :param result_csv_file: string,存放结果的CSV文件路径名
    :param result_html_file: string,存放结果的html文件路径名
    """
    response = requests.get(url)  # 获取每一行的url内容并且调用requests.get方法将调用url相关的内容储存在response变量中。
    if response.history:  # 如果response.history有内容，则说明有重定向发生了。
        write_html(result_html_file,"<p>Request was redirected</p>\n")
        write_csv(result_csv_file,"Request was redirected"+'\n')
        for resp in response.history:  # 重定向的历史
            write_html(result_html_file, '<p>' + resp.url + '->' + '</p>'+'\n')
            write_csv(result_csv_file,resp.url + '->'+'\n')
        write_html(result_html_file, '<p>' + response.url + '</p>' + '&nbsp' +'\n')
        write_csv(result_csv_file, response.url + '\n') # 最终的地址
        write_csv(result_csv_file,"\n") # 写完一个网址的重定向历史后 换行
    else:  # 没有重定向发生，输出没有重定向即可。
        write_html(result_html_file, "<p>Request was not redirected</p>\n")
        write_html(result_html_file,'<p>' + url + '</p>'+ '&nbsp' + '\n') #&nbsp起到空行以示分隔的作用
        write_csv(result_csv_file, "Request was not redirected" +'\n')
        write_csv(result_csv_file,url+'\n')
        # write_html(result_html_file, "<p>1 </p>")
        write_csv(result_csv_file, '\n')  # 写完一个网址的重定向历史后 换行


def multiprocess_get_redirect_history(url_csv_file, result_csv_file, result_html_file):
    """
    多进程获取一个源csv文件中所有url的重定向历史，并写入csv文件和HTML文件中
    :param url_csv_file: string,输入csv文件路径
    :param result_csv_file: string,输出csv文件路径
    :param result_html_file: string,输出html文件路径
    :return: float，花费时间
    """
    start_time = time.time()  # 记录开始时间
    urls = read_csv(url_csv_file)
    numbers_of_url = len(urls)  # 统计url总数
    with open(result_html_file, "w"),open(result_csv_file,'w'):  # 清除输出文件中的陈旧内容
        pass
    write_html(result_html_file, "<html>\
                       <head>redirect history</head>\
                     <body>")  # 将HTML头部先写入HTML文件中
    pool = multiprocessing.Pool(multiprocessing.cpu_count())  # 建立进程池，池大小为cpu个数
    for i in range(numbers_of_url):
        url = urls[i][0]
        pool.apply_async(get_redirect_history, (url, result_csv_file, result_html_file))  # 异步运行
    pool.close()
    pool.join()
    write_html(result_html_file,'''</body>
                   </html>''')  # 在末尾将HTML的尾部补全
    return time.time()-start_time  # 返回花费时间


if __name__ == "__main__":
   multiprocess_get_redirect_history("Proj9_url.csv","Proj9_result.csv","Proj9_result.html")
