from selenium import webdriver
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.chrome.service import Service
import time
import json

import undetected_chromedriver as uc
import pandas as pd


def getChromeDriver():
        service = Service(executable_path=r"D:\devTools\chromedriver_win32112.0.5615.49\chromedriver.exe")
        options = webdriver.ChromeOptions()
# 忽略证书错误
        options.add_argument('--ignore-certificate-errors')
# 忽略 Bluetooth: bluetooth_adapter_winrt.cc:1075 Getting Default Adapter failed. 错误
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 忽略 DevTools listening on ws://127.0.0.1... 提示
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

# options.add_argument('--headless')
        options.binary_location = r"C:\Users\tuday\AppData\Local\Google\Chrome\Application\chrome.exe"

        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        options.add_argument(f"user-agent={ua}")

        driver = webdriver.Chrome(options=options, service=service)

        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
        get: () => false
        })
    """
    })

        return driver

def getData():

    cataUrl = 'https://www.nmpa.gov.cn/datasearch/home-index.html#category={category}'.format(category='ylqx')

# driver = getChromeDriver()
    driver = uc.Chrome()

# ————————————————
# 版权声明：本文为CSDN博主「riwanba」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/riwanba/article/details/131801315

    driver.get(cataUrl)
    cookies = {"name": "STEP_TIPS_INDEX", "value": "true"}
    driver.add_cookie(cookie_dict=cookies)
    cookies = {"name": "STEP_TIPS_RESULT", "value": "true"}
    driver.add_cookie(cookie_dict=cookies)

#隐性等待，在开头设置过之后，整个的程序运行过程中都会有效
    driver.implicitly_wait(100)

    kwInput = driver.find_elements(By.XPATH,'//input[@class="el-input__inner"]')
    kwInput[1].send_keys('山东')

#点击查询
    suBtn = driver.find_elements(By.XPATH,'//div[@class="el-input-group__append"]')
    suBtn[0].find_element(By.TAG_NAME,"button").click()

    time.sleep(5)

    all_handles = driver.window_handles
    #调到列表页
    driver.switch_to.window(all_handles[1])

    #点击详情
    table = driver.find_elements(By.TAG_NAME,"table")
    print(len(table))
    btns = table[1].find_elements(By.TAG_NAME,"button")
    print(len(btns))

    btns[0].click()
    time.sleep(5)
    all_handles = driver.window_handles
    #调到详情页
    driver.switch_to.window(all_handles[2])

    divs = driver.find_elements(By.XPATH,"//div[@class='cell']")
    
    item = {}
    keys = ['注册证编号','注册人名称','注册人住所','生产地址'
,'产品名称'
,'管理类别'
,'型号规格'
,'结构及组成/主要组成成分'
,'适用范围/预期用途'
,'产品储存条件及有效期'
,'附件'
,'其他内容'
,'备注'
,'审批部门'
,'批准日期'
,'生效日期'
,'有效期至'
,'变更情况'
,'注']
    
    #迭代divs
    for i in range(len(divs)):
          if i % 2 == 0:continue
          key = divs[i-1].text
          value = divs[i].text
          item[key]=value

    items = []
    items.append(item)            
    #pd.DataFrame(item).to_excel("nmpa.xls")
    
    df = pd.read_json(json.dumps(items))
    df.index=['row']
    df.to_excel("nmpa.xls",index=True)
    

    time.sleep(5)

if __name__=="__main__":
      getData()

