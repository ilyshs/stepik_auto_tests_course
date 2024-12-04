from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

try:

  button_submit = browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary')
  button_submit.click()

  new_window = browser.window_handles[1]
  first_window = browser.window_handles[0]
  browser.switch_to.window(new_window)

  x_element = browser.find_element(By.ID, 'input_value')
  x_element_value = x_element.text
  y = calc(x_element_value)

  field_for_answer = browser.find_element(By.ID, 'answer')
  field_for_answer.send_keys(y)

  button_submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
  button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(10)
    # закрываем браузер после всех манипуляций
  browser.quit()



