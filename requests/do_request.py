import requests

url = 'https://mp.weixin.qq.com/s?__biz=MzA5MjU2MTAxNQ==&mid=2651059289&idx=1&sn=e2d80f2a08b395553c40189ca0b40b67&chksm=8b9c1f41bceb9657d32363b327baf8e3c081d13e4c8c3c8a09b6d5c049500d2f321133fb989a&scene=126&sessionid=1695194483&subscene=7&clicktime=1695194508&enterid=1695194508&key=b99d03b5a948b092eb9be3839f1793a55b40177fc1213c4726664896f6746fea195769e17e1d962cabd95551ea0cc2f5a73a843f2bbdefd25fb955976dc20f4c05d3bf30a9cf01584e003a41454822850f172e7908d9119a3d7d66da16cc0ba8ad12e393547b3da1e5647fe984ad2443832355bcf9482ccc7162105817dfb097&ascene=0&uin=MjUxNzcwMTk0MQ%3D%3D&devicetype=Windows+11+x64&version=6309070f&lang=zh_CN&countrycode=CN&exportkey=n_ChQIAhIQg5SjW95nEbxlQMZi8ujEyRLgAQIE97dBBAEAAAAAAFh8Mk7pOMYAAAAOpnltbLcz9gKNyK89dVj05Nn%2FC6TNWLi6GuYKiUeJjbX7tjzXtXFCmyblgnuWeH8hZFeFo3tDSIg3Ye8brjuuECEqMgq219XKV11PrU9%2BVJNpz1hcbPLW%2FP7zRs5%2FRmehDbuzpz438a6RHgUQ5Ra26qM7us5BWDlroGDwdKiTqn41geBA6Hg80aVQyTh1wSqzMd33bfcHcFtHphFstuMPe%2BxGczWjQOFnZhrRjr10JTm%2BB3hCSYtrOnlb884stakmVFEWlPN5v%2B5j&acctmode=0&pass_ticket=FzoXLa5xD41QWTTwvlomneGwk%2FbVNqYsiqNjFe5s0bzVUaMEAJ%2FJPfrYaidV887D&wx_header=1&fasttmpl_type=0&fasttmpl_fullversion=6863594-zh_CN-zip&fasttmpl_flag=1'

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