from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #паршу значение
    x_element = browser.find_element_by_css_selector(".form-group #input_value")
    x = x_element.text
    y = calc(x)
    #ввожу в инпут вычисленный ответ
    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector(".form-check-input[type='checkbox']#robotCheckbox")
    option1.click()
    option1 = browser.find_element_by_css_selector(".form-check-input[type='radio']#robotsRule")
    option1.click()

    input2 = browser.find_element_by_css_selector("button[type='submit']")
    input2.click()
 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
