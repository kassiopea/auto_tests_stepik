from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
wd = webdriver.Chrome()
wd.get(link)

# Ваш код, который заполняет обязательные поля
name = wd.find_element_by_css_selector("input[placeholder='Введите имя']")
name.clear()
name.send_keys("Anastasia")
surname = wd.find_element_by_css_selector("input[placeholder='Введите фамилию']")
surname.clear()
surname.send_keys("S")
email = wd.find_element_by_css_selector("input[placeholder='Введите Email']")
email.clear()
email.send_keys("randomnanastya@gmail.com")

# Отправляем заполненную форму
button = wd.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = wd.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
