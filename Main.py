import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe')
        driver = self.driver
        driver.get('https://www.tiendacoomeva.com/')
        driver.maximize_window()
        driver.implicitly_wait(40)

    def test_search_text_field(self):
        search_field = self.driver.find_element(By.XPATH, "//input[@placeholder='¿Qué estás buscando hoy?']")
        search_field.send_keys("ejemplo de búsqueda")
        search_field.submit()

    def test_search_button(self):
        search_button = self.driver.find_element(By.CSS_SELECTOR, 'button.vtex-store-components-3-x-searchBarIcon')
        search_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)

