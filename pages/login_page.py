# login_page.py
from .base_page import BasePage
from ..locators.login_page_locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Abre a página de login ao criar uma instância da classe LoginPage
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        # Insere o nome de usuário no campo de entrada
        username_input = self.wait_for_element((By.ID, LoginPageLocators.USERNAME_INPUT))
        username_input.send_keys(username)

    def enter_password(self, password):
        # Insere a senha no campo de entrada
        password_input = self.wait_for_element((By.ID, LoginPageLocators.PASSWORD_INPUT))
        password_input.send_keys(password)

    def click_login_button(self):
        # Clica no botão de login
        login_button = self.wait_for_element((By.ID, LoginPageLocators.LOGIN_BUTTON))
        login_button.click()
