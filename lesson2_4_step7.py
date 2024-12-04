from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

try:

  price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )

  button_book = browser.find_element(By.ID, 'book')
  button_book.click()

  x_element = browser.find_element(By.ID, 'input_value')
  x_element_value = x_element.text
  y = calc(x_element_value)

  field_for_answer = browser.find_element(By.ID, 'answer')
  field_for_answer.send_keys(y)

  button_submit = browser.find_element(By.ID, 'solve')
  button_submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(10)
    # закрываем браузер после всех манипуляций
  browser.quit()



