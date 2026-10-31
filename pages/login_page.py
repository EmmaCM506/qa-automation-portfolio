from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        
        # Localizadores de los elementos
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']") # Corregido aquí

    def abrir(self):
        self.driver.get(self.url)

    def iniciar_sesion(self, usuario, password):
        self.driver.find_element(*self.username_input).send_keys(usuario)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()