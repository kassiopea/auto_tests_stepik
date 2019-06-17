from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля

# Заполняем поле имя
input1 = browser.find_element_by_xpath("//input[@placeholder='Введите имя']")
input1.send_keys("Ivan")
# Заполняем поле фамилия
input2 = browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']")
input2.send_keys("Petrov")
# Заполняем поле email
input3 = browser.find_element_by_xpath("//input[@placeholder='Введите Email']")
input3.send_keys("test@mail.com")
# Заполняем поле телефон
input4 = browser.find_element_by_xpath("//input[@placeholder='Введите телефон:']")
input4.send_keys("89111234567")
# Заполняем поле адрес
input5 = browser.find_element_by_xpath("//input[@placeholder='Введите адрес:']")
input5.send_keys("Russia Moscow Lesnaya street 2")

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