from selenium import webdriver
import math

wd = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
wd.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


valuex = wd.find_element_by_css_selector("#input_value").text

res = calc(valuex)

input_value = wd.find_element_by_css_selector("#answer")
input_value.send_keys(res)

check = wd.find_element_by_css_selector("#robotCheckbox")
check.click()

radiobutton = wd.find_element_by_css_selector("#robotsRule")
wd.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
radiobutton.click()

button = wd.find_element_by_css_selector("button[type='submit']")
button.click()