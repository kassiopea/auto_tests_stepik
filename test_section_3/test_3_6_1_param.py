import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

testdata = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.fixture(scope="session")
def browser():
    print("\nstart browser")
    browser = webdriver.Chrome(executable_path=r"C:\Tools\Selenium\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('task', testdata)
def test_completed_task(browser, task):
    link = task
    answer = math.log(int(time.time()))
    browser.get(link)
    wait = WebDriverWait(browser, 5)

    input_for_answer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".textarea")))
    input_for_answer.send_keys(str(answer))
    submit_answer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".submit-submission")))
    submit_answer.click()

    with pytest.raises(NoSuchElementException, message="Не должно быть кнопки Отправить"):
        browser.find_element_by_css_selector(".submit-submission")

    test_is_correct = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))).text
    assert test_is_correct == "Correct!", "test is not correct"
