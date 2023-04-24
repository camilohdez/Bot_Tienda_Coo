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

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def test_click_login_button(self):
        driver = self.driver

        # Haz clic en el botón de inicio de sesión
        login_button = self.wait_for_element((By.XPATH, '//button[contains(@class, "vtex-button") and contains(@class, "t-action")]//span[contains(text(), "Entrar")]'))
        login_button.click()

        # Inicia sesión con nombre de usuario y contraseña
        user_name = self.wait_for_element((By.ID, 'username'))
        user_name.clear()
        user_name.send_keys("1006036088")

        password = self.wait_for_element((By.ID,'password'))
        password.clear()
        password.send_keys("Vane-0530.")
        password.send_keys(Keys.RETURN)

        # Espera hasta que la página de inicio de sesión se cargue correctamente
        WebDriverWait(driver, 10).until(EC.title_contains("Coomeva"))

        # Busca productos en la barra de búsqueda
        search_field = self.wait_for_element((By.XPATH, "//input[@placeholder='¿Qué estás buscando hoy?']"))
        search_field.send_keys("celulares")
        search_field.send_keys(Keys.ENTER)

        # Espera hasta que se carguen los resultados de búsqueda
        WebDriverWait(driver, 20).until(EC.title_contains("celulares - Tienda Coomeva"))

        # Filtra los resultados de búsqueda por precio
        search_filters = self.wait_for_element((By.CSS_SELECTOR, 'button.vtex-search-result-3-x-orderByButton'), 20)
        search_filters.click()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)