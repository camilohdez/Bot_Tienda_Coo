import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTests(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.get('https://www.tiendacoomeva.com/')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    def test_click_login_button(self):
        driver = self.driver
        login_form= driver.find_element(By.XPATH, '//button[contains(@class, "vtex-button") and contains(@class, "t-action")]//span[contains(text(), "Entrar")]')
        login_form.click()
        
        user_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'username')))
        user_name.clear()
        user_name.send_keys("1006036088")

        password = driver.find_element(By.ID,'password')
        password.clear()
        password.send_keys("Vane-0530.")
        password.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(EC.title_contains("Coomeva"))

        search_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='¿Qué estás buscando hoy?']")))
        search_field.send_keys("celulares")

        search_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.vtex-store-components-3-x-searchBarIcon')))
        search_button.click()

        WebDriverWait(driver, 20).until(EC.title_contains("celulares - Tienda Coomeva"))

        """search_filter = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button.vtex-search-result-3-x-orderByButton')))
        search_filter.click()"""

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
