from lxml import etree 

import requests

url = "https://www.baidu.com"

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
"""带请求参数"""
params = {'wd':'python'}
response = requests.get('https://www.baidu.com/',params=params,headers=headers)
# print(response.text)

html = etree.HTML(response.text)

# print(html)
r_list = html.xpath('//div[@class="result"]')

for i in r_list :
    print(i)


print(r_list)