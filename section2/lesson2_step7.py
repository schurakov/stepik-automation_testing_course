from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    for selector in ["input[name=firstname]", "input[name=lastname]", "input[name=email]"]:
        input_value = browser.find_element_by_css_selector(selector)
        input_value.send_keys("test")
    
    input1 = browser.find_element_by_css_selector("input[type='file']")
    input1.send_keys(file_path)
    input2 = browser.find_element_by_css_selector("button[type='submit']")
    input2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()