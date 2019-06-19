import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

testdata = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
]


@pytest.mark.parametrize('link', testdata)
def test_exists_the_button_add_to_basket(browser, link):
    browser.get(link)
    wait = WebDriverWait(browser, 5)
    time.sleep(10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")))
