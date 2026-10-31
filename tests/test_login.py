from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_login_exitoso(driver):
    login_page = LoginPage(driver)
    login_page.abrir()
    
    # 1. Ejecutar acción de login
    login_page.iniciar_sesion("standard_user", "secret_sauce")
    
    # 2. Validación explícita: Buscar el título de productos en la página principal
    titulo_productos = driver.find_element(By.CLASS_NAME, "title").text
    
    # 3. Aserción clara (comprobar que el texto sea exactamente "Products")
    assert titulo_productos == "Products", f"Error: Se esperaba ver 'Products' pero se encontró '{titulo_productos}'"
    
    # Si llega aquí, la prueba pasó y sabemos exactamente qué validó.