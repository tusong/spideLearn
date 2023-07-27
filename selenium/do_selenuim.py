from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():
    #使用驱动实例开启会话
    driver = webdriver.Chrome()

#在浏览器上执行操作，这里是导航到一个网页
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#请求 浏览器信息 ；您可以请求一系列关于浏览器的信息 , 包括窗口句柄、浏览器尺寸/位置、cookie、警报等.
    title = driver.title
    assert title == "Web form"

#建立等待策略
    driver.implicitly_wait(0.5)

#查找元素
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#操作元素
    text_box.send_keys("Selenium")
    submit_button.click()

#获取元素信息
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"
#结束会话
    driver.quit()
