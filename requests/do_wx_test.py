import requests

url = 'http://mp.weixin.qq.com/mp/profile_ext'
biz = 'MzA5MjU2MTAxNQ=='
uin = 'MjUxNzcwMTk0MQ=='
key = 'b99d03b5a948b092eb9be3839f1793a55b40177fc1213c4726664896f6746fea195769e17e1d962cabd95551ea0cc2f5a73a843f2bbdefd25fb955976dc20f4c05d3bf30a9cf01584e003a41454822850f172e7908d9119a3d7d66da16cc0ba8ad12e393547b3da1e5647fe984ad2443832355bcf9482ccc7162105817dfb097'
index = 0

offset=0
count=10

params = {
        '__biz': biz,
        'uin': uin,
        'key': key,
        'offset': offset,
        'count': count,
        'action': 'getmsg',
        'f': 'json'
    }


header = {
    "Host": "mp.weixin.qq.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8431 Flue",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
    }
cookie = {
    "wxuin": "2517701941",
    "devicetype": "Windows11x64",
    "version": "6309070f",
    "lang": "zh_CN",
    "rewardsn": "",
    "wxtokenkey": "777",
    "appmsg_token": "1236_t2r0eHTdr0M7juUYovzuyoeaHuWinStmaYd-eiFInfrwPPGJvAUAMSn9tPBoAinjEcgcH9rnVIn__WKP",
    "pass_ticket": "wKd+GqIDl5YiFmpqVIKG1OWN1rqr8fCSMqGR7Qg4HoAg8O+NAJBqQv43SnRBSvSx",
    "wap_sid2": "CLWqxLAJEooBeV9ITk1xQllfZW5IY0p4bF83SDkyUFNZanVXbnVpQmpIa2lEMFEtSDN1ckZSektMMWxkVlZfRFp2TWUyX0dUODc0d1Y0YXJTWklqS2gyZlg0czVBUVVYZDNER2RnU3VybDl2Wm1DckZGUEhqT0FtUnpiVWVVN0VkS1V0cFVadXJQYUJiRVNBQUF+MMy4qqgGOA1AAQ=="
}
#verify = False 去掉ssl证书校验
response = requests.get(url,headers=header,cookies=cookie,verify = False)
print(response.text)