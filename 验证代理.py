import requests
import re
requests.packages.urllib3.disable_warnings


def url_response(url='https://httpbin.org/ip', proxy=None):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    proxies = {
        'http': '{}'.format(proxy), 
        'https': '{}'.format(proxy)
    }
    try:
        if proxy:
            response = requests.get(url, headers=header, proxies=proxies, timeout=10)
            print(proxy)
            fover.write(proxy +"\n")
            return "YES"
        else:
            response = requests.get(url, headers=header, timeout=5)
            print(proxy)
            return "YES"
    except:
        return None

    return response  #该函数放回response响应


ff = open("list.txt","r")
fover = open("over.txt","w")
a =  ff.read().splitlines()
print(a)
j=0
while j<10 :
    url_response(url="https://baidu.com",proxy="http://" +a[j])
    j = j+1
ff.close
fover.close


