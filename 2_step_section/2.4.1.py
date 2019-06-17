from selenium import webdriver

wd = webdriver.Chrome()
wd.implicitly_wait(5)
wd.get("http://suninjuly.github.io/cats.html")

wd.find_element_by_id("button")