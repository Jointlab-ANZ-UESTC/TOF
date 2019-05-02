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
            writer = csv.writer(f)
            writer.writerow(content)


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


def get_status(url):
    """

    :param url: string,需要得到状态的url
    :return: list,[url,状态码]
    """
    r = requests.get(url)
    return [url, r.status_code]


def process_get_status(url, written_file):
    """
    单个进程运行的获得url状态并将之写入csv文件的函数
    :param url: string,url
    :param written_file: string,被写文件路径名
    :return: void
    """
    status_list = get_status(url)
    write_csv(written_file, status_list)


def multiprocess_get_status(read_path, out_path):
    """
    多进程获取一个源csv文件中所有url的状态，并写入另一个csv文件中
    :param read_path: string,源csv文件路径
    :param out_path: string,输出csv文件路径
    :return: float，花费时间
    """
    start_time = time.time()  # 记录开始时间
    urls = read_csv(read_path)
    numbers_of_url = len(urls)  # 统计url总数
    with open(out_path, "w"):  # 清除输出文件中的陈旧内容
        pass
    pool = multiprocessing.Pool(multiprocessing.cpu_count())  # 建立进程池，池大小为cpu个数
    for i in range(numbers_of_url):
        url = urls[i][0]
        pool.apply_async(process_get_status, (url, out_path,))  # 异步运行
    pool.close()
    pool.join()
    return time.time()-start_time  # 返回花费时间


if __name__ == "__main__":
    print(multiprocess_get_status("C:\\Users\顾先生\\Desktop\\input file for ticket2.csv",
                                  "C:\\Users\顾先生\\Desktop\\out.csv"))
