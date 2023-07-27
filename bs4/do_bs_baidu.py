import requests

url = "https://www.baidu.com/s"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Cookie':'BIDUPSID=C088B2ED7B6ACB72824331A2C155B270; PSTM=1684221057; BAIDUID=C088B2ED7B6ACB7253362ABAB5529839:FG=1; BAIDUID_BFESS=C088B2ED7B6ACB7253362ABAB5529839:FG=1; ZFY=mrwtqx07rmCnce6v7pL34nvnVIOGG6uC:Ap:BjZCcU:A8Q:C; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; PSINO=6; H_PS_PSSID=36552_38643_38831_39114_39117_39088_26350_39050_22160_39100_39044; BD_UPN=12314753; H_PS_645EC=0bf4jBg6%2BKSroVr3eH46JuO3I2c7IcILvB1Lqa%2Be%2B2hpglNhIwuhQY6IvLG0YdrESUXX; BA_HECTOR=al8kag0k01ag81248g80a5041ibufc01o; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598'}
    

"""带请求参数"""
params = {'wd':'python'}
response = requests.get(url,params=params,headers=headers)
# print(response.text)

from bs4 import BeautifulSoup
htmlStr = response.text

with open("aa.html","w",encoding="utf-8") as f:
    f.write(htmlStr)

soup = BeautifulSoup(htmlStr,'html.parser')
#print(soup.prettify())

result = soup.find_all('div')
print(len(result))