import re
from time import sleep
import requests
from lxml import etree
#调用https://proxy.seofangfa.com/
headerss = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}
url = 'https://proxy.seofangfa.com/'
pa_re = requests.get(url,headers=headerss)
pa_re.encoding = ("UTF-8")
obj = re.compile(r".*?<tr><td>(?P<ip>.*?)</td><td>(?P<port>.*?)</td><td>.*?</td><td>.*?</td><td>.*?</td></tr>",re.S)
ipport = obj.findall(pa_re.text)

print(ipport[0][0])
f = open("list.txt","w")
i=0
while i< 10 :
    f.write(ipport[i][0])   #写入ip
    f.write(":")            #写入分隔符
    f.write(ipport[i][1])   #写入端口
    f.write("\n")
    i = i+1
# ------------------------------------------------------------------------------------------------------------------#
#调用齐云代理
obj2 = re.compile(r"<td data-title=\"IP\">(?P<ip>.*?)</td>.*?<td data-title=\"PORT\">(?P<port>.*?)</td>.*?<td data-title=\"类型\">HTTPS.*?</tr>",re.S)
i=1
while i<=5 :            #为了确保数据是近期的，所以只爬五页
    urll = f"https://proxy.ip3366.net/free/?action=china&page={i}"
    urll_re = requests.get(urll,headers=headerss)
    urll_re.encoding = ("UTF-8")
    
    ipport = obj2.findall(urll_re.text)
    print(ipport)
    j=0
    while j < len(ipport):
        f.write(ipport[j][0])
        f.write(ipport[j][1]) 
        f.write("\n")
        j = j+1
    i = i+1
# ------------------------------------------------------------------------------------------------------------------#
#ip3366
urlll = "http://www.ip3366.net/free/?page=1"
urlll_re = requests.get(urlll,headers=headerss)
urlll_re.encoding = ("gb2312")

urlll_etree = etree.HTML(urlll_re.text)
urlll_ip  = urlll_etree.xpath("/html/body/div[2]/div/div[2]/table/tbody/tr[*]/td[1]/text()")
urlll_port = urlll_etree.xpath("/html/body/div[2]/div/div[2]/table/tbody/tr[*]/td[2]/text()")
urlll_type = urlll_etree.xpath("/html/body/div[2]/div/div[2]/table/tbody/tr[*]/td[4]/text()")

k=0
while k < len(urlll_type) :
    if urlll_type[k] == "HTTPS" :
        f.write(urlll_ip[k])
        f.write(":")
        f.write(urlll_port[k])
        f.write("\n")
    k = k+1
# ------------------------------------------------------------------------------------------------------------------#




f.close