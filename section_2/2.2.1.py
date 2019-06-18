from selenium import webdriver
from selenium.webdriver.support.ui import Select


def sum_int(numb1, numb2):
    return str(int(numb1) + int(numb2))


wd = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
wd.get(link)

num1 = wd.find_element_by_css_selector("#num1").text
num2 = wd.find_element_by_css_selector("#num2").text

res = sum_int(num1, num2)

Select(wd.find_element_by_css_selector("#dropdown")).select_by_value(res)

button = wd.find_element_by_css_selector("button[type='submit']")
button.click()
