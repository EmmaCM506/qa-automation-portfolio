from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        # El título de la página de inventario después del login exitoso
        self.titulo_inventario = (By.CSS_SELECTOR, ".title")
        # El contenedor del mensaje de error para logins fallidos
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def abrir(self):
        self.driver.get(self.url)

    def iniciar_sesion(self, usuario, password):
        self.driver.find_element(*self.username_input).send_keys(usuario)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def obtener_titulo_productos(self):
        # Espera explícita: espera máximo 10 segundos a que el elemento .title sea visible
        elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.titulo_inventario)
        )
        return elemento.text
    
    def obtener_error(self):
        # Espera explícita para asegurar que el mensaje de error aparezca en pantalla
        elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        )
        return elemento.text