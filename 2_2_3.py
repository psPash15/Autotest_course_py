from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def sum (number1, number2):
 return str(number1+number2)

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    number1 = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    #num1 = number1.get_attribute(".text()")
    number2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    #num2 = number2.get_attribute(".text()")

    y = sum(number1, number2)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y)) 

    # Ваш код, который заполняет обязательные поля

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()