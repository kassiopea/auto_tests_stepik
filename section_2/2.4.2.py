from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


wd = webdriver.Chrome()
wd.get("http://suninjuly.github.io/explicit_wait2.html")

button = wd.find_element_by_css_selector("#book")

WebDriverWait(wd, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))

button.click()

elem = WebDriverWait(wd, 5).until(EC.visibility_of_element_located((By.ID, "input_value")))

res = calc(elem.text)

input_value = wd.find_element_by_css_selector("#answer")
input_value.send_keys(res)

button_sumbit = wd.find_element_by_css_selector("#solve")
button_sumbit.click()


