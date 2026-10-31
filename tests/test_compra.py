from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_agregar_producto_al_carrito(driver):
    # 1. Iniciar sesión con éxito
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.iniciar_sesion("standard_user", "secret_sauce")

    # 2. Interactuar con la página de inventario
    inventory_page = InventoryPage(driver)
    
    # Validar que entramos a la tienda
    assert "Products" in inventory_page.obtener_titulo()

    # Agregar la mochila al carrito
    inventory_page.agregar_primer_producto()
    inventory_page.ir_al_carrito()

    # Validar que estamos en el carrito (o que el producto fue añadido)
    # Aquí puedes agregar una pequeña validación de URL o elementos del carrito
    assert "cart.html" in driver.current_url