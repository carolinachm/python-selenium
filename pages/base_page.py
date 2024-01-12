# base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        # Inicializa a página base com o driver
        self.driver = driver

    def wait_for_element(self, locator):
        # Aguarda até que o elemento esteja presente na página
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
