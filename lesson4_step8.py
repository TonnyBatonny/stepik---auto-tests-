import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
      )
    book_btn = browser.find_element_by_id("book")
    book_btn.click()
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    answer_input = browser.find_element_by_css_selector('#answer')
    answer_input.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()
finally:

    time.sleep(10)
    browser.quit()