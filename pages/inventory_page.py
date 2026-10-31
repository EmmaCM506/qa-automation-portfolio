from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        # Localizadores
        self.titulo_pagina = (By.CLASS_NAME, "title")
        self.primer_producto_agregar = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.carrito_icono = (By.CLASS_NAME, "shopping_cart_link")

    def obtener_titulo(self):
        return self.driver.find_element(*self.titulo_pagina).text

    def agregar_primer_producto(self):
        self.driver.find_element(*self.primer_producto_agregar).click()

    def ir_al_carrito(self):
        self.driver.find_element(*self.carrito_icono).click()