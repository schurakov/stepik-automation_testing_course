from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x, y):
  return x + y

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1")
    x_num = x.text
    y = browser.find_element_by_id("num2")
    y_num = y.text
    xy = calc(int(x_num), int(y_num))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(xy))

    browser.find_element_by_xpath("//button[text()='Submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
