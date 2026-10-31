from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_flujo_compra_exitoso(driver):
    # 1. Iniciar sesión
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.iniciar_sesion("standard_user", "secret_sauce")

    # 2. Agregar producto al carrito y navegar al carrito
    inventory_page = InventoryPage(driver)
    assert "Products" in inventory_page.obtener_titulo()
    inventory_page.agregar_primer_producto()
    inventory_page.ir_al_carrito()

    # 3. Ir al Checkout y llenar los datos de envío
    checkout_page = CheckoutPage(driver)
    checkout_page.ir_al_checkout()
    checkout_page.llenar_datos_envio("Emmanuel", "Calvo", "10101")

    # 4. Finalizar la compra
    checkout_page.finalizar_compra()

    # 5. Validar el mensaje de éxito de la orden completada
    mensaje_exito = checkout_page.obtener_mensaje_exito()
    assert "Thank you for your order!" in mensaje_exito, f"El mensaje obtenido fue: {mensaje_exito}"