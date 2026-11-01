from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        # Localizadores
        self.titulo_pagina = (By.CLASS_NAME, "title")
        self.primer_producto_agregar = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.carrito_icono = (By.CLASS_NAME, "shopping_cart_link")
        self.carrito_contador = (By.CLASS_NAME, "shopping_cart_badge")

    def obtener_titulo(self):
        return self.wait.until(EC.visibility_of_element_located(self.titulo_pagina)).text

    def agregar_primer_producto(self):
        self.wait.until(EC.element_to_be_clickable(self.primer_producto_agregar)).click()
        self.wait.until(
            EC.visibility_of_element_located(self.carrito_contador),
            message="Se hizo click en 'Add to cart' pero el contador del carrito no apareció",
        )

    def ir_al_carrito(self):
        self.wait.until(EC.element_to_be_clickable(self.carrito_icono)).click()
        self.wait.until(
            EC.url_contains("cart.html"),
            message="Se hizo click en el carrito pero la URL no cambió a cart.html",
        )