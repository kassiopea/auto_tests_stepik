from selenium import webdriver
import math

wd = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
wd.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


button = wd.find_element_by_css_selector(".trollface")
button.click()

new_window = wd.window_handles[1]

wd.switch_to.window(new_window)

value = wd.find_element_by_css_selector("#input_value").text
x = calc(value)

input_for_answer = wd.find_element_by_css_selector("#answer")
input_for_answer.send_keys(x)

button_submit = wd.find_element_by_css_selector("button[type='submit']")
button_submit.click()
