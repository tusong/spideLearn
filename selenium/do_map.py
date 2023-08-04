from selenium import webdriver
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions
import time

import pandas as pd

cityStr = input("请输入城市：")

options = EdgeOptions()
options.use_chromium = True
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" # 浏览器的位置
driver = Edge(options=options, executable_path=r"D:\devTools\edgedriver_win64\msedgedriver.exe") # 相应的浏览器的驱动位置

driver.get("https://map.baidu.com")

#建立等待策略
driver.implicitly_wait(2)

#关闭框
driver.find_element_by_id('TANGRAM__PSP_37__closeBtn').click()


#city_change按钮，点击会弹出城市选择
cityChange = driver.find_element_by_xpath("//a[@class='ui3-city-change-inner ui3-control-shadow']")
cityChange.click()

time.sleep(5)
city_sel = driver.find_element_by_id('selCityPlaceListId')
city = city_sel.find_element_by_xpath("(//a[contains(text(),'%s')])" % cityStr)
city.click()


time.sleep(2)

driver.find_element_by_id('sole-input').click()
driver.find_element_by_xpath("//div[@data-key='美食']").click()
print("点击美食")

