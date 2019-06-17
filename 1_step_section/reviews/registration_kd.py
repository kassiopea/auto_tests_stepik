from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element_by_css_selector("[placeholder='Введите имя']")
input1.send_keys("Имя")
input2 = browser.find_element_by_css_selector("[placeholder='Введите фамилию']")
input2.send_keys("Фамилия")
input3 = browser.find_element_by_css_selector("[placeholder='Введите Email']")
input3.send_keys("email@mail.com")
input4 = browser.find_element_by_css_selector("[placeholder='Введите телефон:']")
input4.send_keys("8-800-555-55-55")
input5 = browser.find_element_by_css_selector("[placeholder='Введите адрес:']")
input5.send_keys("Страна, Город, улица, дом 15, кв.6")

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text