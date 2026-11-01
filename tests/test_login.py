from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_login_exitoso(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.abrir()
    login_page.iniciar_sesion("standard_user", "secret_sauce")

    titulo = inventory_page.obtener_titulo()
    assert titulo == "Products", f"Se esperaba 'Products' pero se encontró '{titulo}'"