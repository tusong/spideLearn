from selenium import webdriver
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.chrome.service import Service
import time

import pandas as pd

cityStr = input("请输入城市：")
if cityStr =="" :
        cityStr="北京"

# options = EdgeOptions()
# options.use_chromium = True
# options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" # 浏览器的位置
# driver = Edge(options=options, executable_path=r"D:\devTools\edgedriver_win64\msedgedriver.exe") # 相应的浏览器的驱动位置

# driver = webdriver.Chrome(r"D:\devTools\chromedriver_win32\chromedriver.exe")

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

driver = webdriver.Chrome(options=options, service=service)

driver.get("https://map.baidu.com")

#隐式等待，单位是秒
driver.implicitly_wait(2)

#关闭框
driver.find_element(By.ID,'TANGRAM__PSP_37__closeBtn').click()


#city_change按钮，点击会弹出城市选择
cityChange = driver.find_element(By.XPATH,"//a[@class='ui3-city-change-inner ui3-control-shadow']")
cityChange.click()

time.sleep(5)
city_sel = driver.find_element(By.ID,'selCityPlaceListId')
city = city_sel.find_element(By.XPATH,"(//a[contains(text(),'%s')])" % cityStr)
city.click()


time.sleep(2)

driver.find_element(By.ID,'sole-input').click()
driver.find_element(By.XPATH,"//div[@data-key='美食']").click()
print("点击美食")
time.sleep(2)

titles = driver.find_elements(By.XPATH,"//a[@class='n-blue']")
scores = driver.find_elements(By.XPATH,"//span[@class='score']")
prices = driver.find_elements(By.XPATH,"//span[@class='d-red']")
addrs = driver.find_elements(By.XPATH,"//span[@class='n-grey']")

# print([ x.text for x in titles])

data = {'店名':[ x.text for x in titles],'评分':[ x.text for x in scores],'价格':[ x.text for x in titles]
        ,'地址':[ x.text for x in addrs]}

pd.DataFrame(data).to_excel("百度地图美食.xls")