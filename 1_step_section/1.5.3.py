from selenium import webdriver

wd = webdriver.Chrome()
wd.get("http://suninjuly.github.io/huge_form.html")
elements = wd.find_elements_by_tag_name("input")
for element in elements:
    element.send_keys("Мой ответ")

button = wd.find_element_by_css_selector("button.btn")
button.click()
