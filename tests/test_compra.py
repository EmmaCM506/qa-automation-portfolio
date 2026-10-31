from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_agregar_producto_al_carrito(driver):
    # 1. Iniciar sesión con éxito
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.iniciar_sesion("standard_user", "secret_sauce")

    # 2. Interactuar con la página de inventario
    inventory_page = InventoryPage(driver)
    
    # Validar que entramos a la tienda
    assert "Products" in inventory_page.obtener_titulo()

    # Agregar la mochila al carrito y navegar
    inventory_page.agregar_primer_producto()
    inventory_page.ir_al_carrito()

    # 3. Espera explícita para asegurar la transición de URL en entornos de CI/CD
    WebDriverWait(driver, 10).until(
        EC.url_contains("cart.html")
    )

    # Validar que estamos en el carrito
    assert "cart.html" in driver.current_url