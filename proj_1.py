import requests
import argparse
import csv


# res = requests.get('http://www.apache.org/guyuhao')
#
# status_code = res.status_code
#
# print(status_code)

results = list()

with open('test.csv') as f:
    reader = csv.reader(f)
    urls = [x for x in reader]
    for url in urls:
        url = url[0]
        res = requests.get(url)
        status_code = res.status_code
        results.append([url, status_code])
    if results == 200:
        print("OK")
    else:
        print("the HTTP Status Code is not 200")
    with open('results.csv', 'w+') as f:
        writer = csv.writer(f)
        writer.writerows(results)
