# test_login.py
import unittest
from selenium import webdriver
from ..pages.login_page import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        # Configuração: Inicializa o driver do Chrome e a página de login
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        # Teste: Realiza um login bem-sucedido
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login_button()

        # Adicione verificações adequadas para garantir o login bem-sucedido

    def tearDown(self):
        # Limpeza: Fecha o navegador após o teste
        self.driver.quit()

if __name__ == "__main__":
    # Executa os testes
    unittest.main()
