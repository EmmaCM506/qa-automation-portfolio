from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.success_message = (By.CLASS_NAME, "complete-header")

    def ir_al_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

    def llenar_datos_envio(self, nombre, apellido, codigo_postal):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        ).send_keys(nombre)
        self.driver.find_element(*self.last_name_input).send_keys(apellido)
        self.driver.find_element(*self.postal_code_input).send_keys(codigo_postal)
        self.driver.find_element(*self.continue_button).click()

    def finalizar_compra(self):
        # Espera explícita para asegurar que el botón Finish esté listo para recibir el clic
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()

    def obtener_mensaje_exito(self):
        # Espera explícita para asegurar que cargue la pantalla final de confirmación
        elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.success_message)
        )
        return elemento.text