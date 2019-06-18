from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


wd = webdriver.Chrome()
link = "http://suninjuly.github.io/math.html"
wd.get(link)
x = wd.find_element_by_css_selector("#input_value").text
res = calc(x)
input_res = wd.find_element_by_css_selector("#answer")
input_res.send_keys(res)

check = wd.find_element_by_css_selector("#robotCheckbox")
check.click()

radiobutton = wd.find_element_by_css_selector("#robotsRule")
radiobutton.click()

button = wd.find_element_by_css_selector("button[type='submit']")
button.click()
