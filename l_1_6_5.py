from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")

print(str(math.ceil(math.pow(math.pi, math.e)*10000)))

try:
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = browser.find_element(By.NAME, 'first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, 'firstname')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

