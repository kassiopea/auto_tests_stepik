from selenium import webdriver
import math

wd = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
wd.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


button = wd.find_element_by_css_selector("button[type='submit']")
button.click()

alert = wd.switch_to.alert
alert.accept()

value = wd.find_element_by_css_selector("#input_value").text

x = calc(value)

input_answer = wd.find_element_by_css_selector("#answer")
input_answer.send_keys(x)

button_submit_form = wd.find_element_by_css_selector("button[type='submit']")
button_submit_form.click()

