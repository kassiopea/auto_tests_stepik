from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


wd = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"
wd.get(link)

x = wd.find_element_by_css_selector("#treasure").get_attribute("valuex")
res = calc(x)

input_value = wd.find_element_by_id("answer")
input_value.send_keys(res)

check = wd.find_element_by_id("robotCheckbox")
check.click()

radiobutton = wd.find_element_by_id("robotsRule")
radiobutton.click()

button = wd.find_element_by_css_selector("button[type='submit']")
button.click()
