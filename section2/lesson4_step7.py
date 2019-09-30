from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)



    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button_book = browser.find_element_by_css_selector("button#book")
    button_book.click()
    
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