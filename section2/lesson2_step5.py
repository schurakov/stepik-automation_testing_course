from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #паршу значение
    x_element = browser.find_element_by_id("input_value")
    x = calc(int(x_element.text))
    #ввожу в инпут вычисленный ответ
    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(x)

    option1 = browser.find_element_by_css_selector("#robotCheckbox[type='checkbox']")
    option1.click()
    option1 = browser.find_element_by_css_selector("#robotsRule[type='radio']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()

    input2 = browser.find_element_by_css_selector("button[type='submit']")
    input2.click()
 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
