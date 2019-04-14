import multiprocessing
import requests
import csv
import time


def write_csv(written_file, content):
        with open(written_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(content)


def read_csv(read_file):
    with open(read_file, "r") as f:
        reader = csv.reader(f)
        content = list(reader)
        return content


def get_status(url):
    r = requests.get(url)
    return [url, r.status_code]


def process_get_status(url, written_file):
    status_list = get_status(url)
    write_csv(written_file, status_list)


def multiprocess_get_status(read_path, out_path):
    start_time = time.time()
    urls = read_csv(read_path)
    numbers_of_url = len(urls)
    with open(out_path, "w"):
        pass
    pool = multiprocessing.Pool(4)
    for i in range(numbers_of_url):
        url = urls[i][0]
        pool.apply_async(process_get_status, (url, out_path,))
    pool.close()
    pool.join()
    return time.time()-start_time
