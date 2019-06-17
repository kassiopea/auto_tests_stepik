from selenium import webdriver
import os

wd = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
wd.get(link)

name = wd.find_element_by_name("firstname")
name.send_keys("Anastasia")
lastname = wd.find_element_by_name("lastname")
lastname.send_keys("Salikova")
email = wd.find_element_by_name("email")
email.send_keys("randomnanastya@gmail.com")

upload_file = wd.find_element_by_css_selector("#file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file = os.path.join(current_dir, 'empty_file.txt')
upload_file.send_keys(file)

button = wd.find_element_by_css_selector("button[type='submit']")
button.click()

