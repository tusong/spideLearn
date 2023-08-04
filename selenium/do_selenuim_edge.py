from selenium import webdriver
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions
import time

import pandas as pd


def get_data():
    pass

options = EdgeOptions()
options.use_chromium = True
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" # 浏览器的位置
driver = Edge(options=options, executable_path=r"D:\devTools\edgedriver_win64\msedgedriver.exe") # 相应的浏览器的驱动位置

driver.get("http://www.baidu.com")

kwInput = driver.find_element_by_xpath('//*[@id="kw"]')
kwInput.send_keys('python')

#点击查询
suBtn = driver.find_element_by_xpath('//*[@id="su"]')
suBtn.click()

#建立等待策略
driver.implicitly_wait(2)

elements = driver.find_elements_by_xpath('//div[@class="c-container"]')

print(len(elements))


titles = list()
links = list()
contents = list()

for element in elements :
    a = element.find_element(By.TAG_NAME,'a')
    # print('标题：%s' % a.text)
    # print('链接：%s' % a.get_attribute('href'))
    content = element.find_element(By.CLASS_NAME,'content-right_8Zs40')
    # print('内容:%s' % content.text)

    titles.append(a.text)
    links.append(a.get_attribute('href'))
    contents.append(content.text)

#分页
for i in range(1,9) :
    pageBtn = driver.find_elements_by_xpath('//span[@class="page-item_M4MDr pc"]') 
    pageBtn[i].click()
    time.sleep(5)
    elements = driver.find_elements_by_xpath('//div[@class="c-container"]')
    print(len(elements))

    for element in elements :
        a = element.find_element(By.TAG_NAME,'a')
        # print('标题：%s' % a.text)
        # print('链接：%s' % a.get_attribute('href'))
        content = element.find_element(By.CLASS_NAME,'content-right_8Zs40')
        # print('内容:%s' % content.text)
        titles.append(a.text)
        links.append(a.get_attribute('href'))
        contents.append(content.text)

data = {'titles':titles,'links':links,'contents':contents}

pd.DataFrame(data).to_excel("a.xls")