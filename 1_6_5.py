from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 
import math

link = "https://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    input2 = browser.find_element(By.NAME, "first_name")
    input2.send_keys("Ivan")
    input3 = browser.find_element(By.NAME, "last_name")
    input3.send_keys("Petrov")
    input4 = browser.find_element(By.CLASS_NAME, "city")
    input4.send_keys("Smolensk")
    input5 = browser.find_element(By.ID, "country")
    input5.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла