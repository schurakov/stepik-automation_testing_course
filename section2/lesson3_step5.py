from selenium import webdriver
import time
import os
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    #паршу значение
    x_element = browser.find_element_by_id("input_value")
    x = calc(int(x_element.text))

    #ввожу в инпут вычисленный ответ
    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(x)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()