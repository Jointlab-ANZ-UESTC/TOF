import requests
import proj4_redirect_history


def set_proxy():
    global proxy    # 定义全局变量，供函数修改以及主代码块的使用。
    proxy_ip = input('please enter the proxy server ip address:')   # 输入服务器的ip地址
    proxy_port = input('please enter the proxy sever''s port')  # 输入服务器的端口地址
    proxy_name = input('please enter the proxy''s user name')   # 输入服务器的用户名
    proxy_password = input('please enter the proxy''s user''s password')    # 输入服务器的用户密码
    proxy = {   # 设置代理服务器的用户名，密码，ip，端口。
        'http':'http://${0}:${1}@${2}:${3}/'.format(proxy_name,proxy_password,proxy_ip,proxy_port)
    }


if __name__ == '__main__':
    set_proxy()
    requests.get('http://example.org',proxies=proxy)
