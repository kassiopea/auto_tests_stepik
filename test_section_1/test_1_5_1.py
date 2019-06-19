from selenium import webdriver

link = "http://suninjuly.github.io/simple_form_find_task.html"
wd = webdriver.Chrome()
wd.get(link)

input1 = wd.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = wd.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = wd.find_element_by_class_name("city")
input3.send_keys("Smolensk")
input4 = wd.find_element_by_id("country")
input4.send_keys("Russia")
button = wd.find_element_by_css_selector("button.btn")
button.click()
