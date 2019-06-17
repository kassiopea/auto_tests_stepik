from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
input_name = browser.find_element_by_xpath("//input[contains(@placeholder, 'Введите имя')]")
input_name.send_keys("Name")

input_surname = browser.find_element_by_xpath("//input[contains(@placeholder, 'Введите фамилию')]")
input_surname.send_keys("Surname")

input_name = browser.find_element_by_xpath("//input[contains(@placeholder, 'Введите Email')]")
input_name.send_keys("test@test.org")

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