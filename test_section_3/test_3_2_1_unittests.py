from selenium import webdriver
import unittest


class TestSection(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Chrome("C:\Tools\Selenium\chromedriver.exe")

    def register_user(self, url):
        wd = self.wd
        wd.get(url)
        name = wd.find_element_by_css_selector(".first_block .first_class .first")
        name.clear()
        name.send_keys("Anastasia")
        last_name = wd.find_element_by_css_selector(".first_block .second_class .second")
        last_name.clear()
        last_name.send_keys("S")
        email = wd.find_element_by_css_selector(".first_block .third_class .third")
        email.clear()
        email.send_keys("randomnanastya@gmail.com")

        button = wd.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = wd.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        return welcome_text

    def test_register(self):
        res = self.register_user("http://suninjuly.github.io/registration1.html")
        mes = "Поздравляем! Вы успешно зарегистировались!"

        self.assertEqual(res, mes, "failed to register")

    def test_error_register(self):
        res = self.register_user("http://suninjuly.github.io/registration2.html")
        mes = "Поздравляем! Вы успешно зарегистировались!"
        self.assertEqual(res, mes, "failed to register")


if __name__ == "__main__":
    unittest.main()
