import requests
from bs4 import BeautifulSoup
 
def get_baidu_search_result(keyword):
    url = 'https://www.baidu.com/s'
    params = {'wd': keyword}
    headers = {'User-Agent': 'Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
               'Accept':
'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
'Accept-Encoding':
'gzip, deflate, br',
'Accept-Language':
'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Cache-Control':
'no-cache',
'Pragma':
'no-cache',
'Referer':
'',
'Cookie':'BIDUPSID=C088B2ED7B6ACB72824331A2C155B270; PSTM=1684221057; BAIDUID=C088B2ED7B6ACB7253362ABAB5529839:FG=1; BAIDUID_BFESS=C088B2ED7B6ACB7253362ABAB5529839:FG=1; ZFY=mrwtqx07rmCnce6v7pL34nvnVIOGG6uC:Ap:BjZCcU:A8Q:C; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; PSINO=6; H_PS_PSSID=36552_38643_38831_39114_39117_39088_26350_39050_22160_39100_39044; BD_UPN=12314753; H_PS_645EC=0bf4jBg6%2BKSroVr3eH46JuO3I2c7IcILvB1Lqa%2Be%2B2hpglNhIwuhQY6IvLG0YdrESUXX; BA_HECTOR=al8kag0k01ag81248g80a5041ibufc01o; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598'}
    response = requests.get(url, params=params, headers=headers)

    with open("aa.html","w",encoding="utf-8") as f:
        f.write(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())
    results = soup.find_all('div', class_='result')
    for result in results:
        try:
            title = result.h3.a.text
            link = result.h3.a['href']
            desc = result.find('div', class_='c-abstract').text
            print(title)
            print(link)
            print(desc)
        except:
            pass
 
if __name__ == '__main__':
    keyword = 'Python'
    get_baidu_search_result(keyword)