from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #паршу значение
    x_element = browser.find_element_by_css_selector("img#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    #ввожу в инпут вычисленный ответ
    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector("#robotCheckbox[type='checkbox']")
    option1.click()
    option1 = browser.find_element_by_css_selector("#robotsRule[type='radio']")
    option1.click()

    input2 = browser.find_element_by_css_selector("button[type='submit']")
    input2.click()
 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
