"""get请求"""
import requests

url = 'https://tse4-mm.cn.bing.net/th/id/OIP-C.w3cHPxIHKpLZodnlBoIZXgHaMx?w=182&h=314&c=7&o=5&dpr=1.45&pid=1.7'
response = requests.get(url)
print(response.status_code)

"""添加请求头：header"""
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
response = requests.get('https://www.zhihu.com/explore',headers=headers)
print(response.status_code)

"""带请求参数"""
params = {'wd':'python'}
response = requests.get('https://www.baidu.com/',params=params)
print(response.status_code)

"""代理设置"""
proxies = {'http':'http://127.0.0.1:9743',
          'https':'https://127.0.0.1:9742',}
response = requests.get('https://www.taobao.com',proxies=proxies)
print(response.status_code)

"""SSL证书验证"""
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)

"""超时设置"""
try:
    response = requests.get("http://httpbin.org/get", timeout = 0.5)
    print(response.status_code)
except requests.exceptions.ReadTimeout:
    print('timeout')

"""认证设置"""
response = requests.get("http://120.27.34.24:9001/",auth=requests.auth.HTTPBasicAuth("user","123"))
print(response.status_code)

"""post请求"""

import requests
import json

host = 'http://httpbin.org/'
endpoint = 'post'
url = ''.join([host,endpoint])

"""带数据的post"""
data = {'key1':'value1','key2':'value2'}
response = requests.post(url,data=data)
print(response.status_code)
print(response.text)

"""带headers的post"""
headers = {'User-Agent':'test request headers'}
response = requests.post(url,headers=headers)
print(response.status_code)
print(response.text)

"""带json的post"""
data = {
    'sites':[
        {'name':'test','url':'www.test.com'},
        {'name':'google','url':'www.google.com'},
        {'name':'weibo','url':'www.weibo.com'}
    ]
}
response = requests.post(url,json=data)
print(response.status_code)
print(response.text)

"""带参数的post"""
params = {'key1':'params1','key2':'params'}
response = requests.post(url,params=params)
print(response.status_code)
print(response.text)

"""文件上传"""
files = {'file':open('fisrtgetfile.txt','rb')}
response = requests.post(url,files=files)
print(response.status_code)
print(response.text)

"""put请求"""
import requests 
import json

url = 'http://127.0.0.1:8080'
header = {'Content-Type':'application/json'}
param = {'myObjectField':'hello'}
payload = json.dumps(param)

response = requests.put(url,data=payload,headers=headers)

"""head请求"""
import requests

response = requests.head('https://pixabay.com/zh/')
print(response.status_code)

"""delete请求"""
import requests

url = 'https://api.github.com/user/emails'
email = '2475757652@qq.com'

response = requests.delete(url,json=email,auth=('username','password'))
print(response.status_code)

"""options请求"""
import requests
import json

url = 'https://www.baidu.com/s'
response = requests.options(url)
print(response.status_code)