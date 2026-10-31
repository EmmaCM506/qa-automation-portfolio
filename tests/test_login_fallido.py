from pages.login_page import LoginPage

def test_login_usuario_bloqueado(driver):
    login_page = LoginPage(driver)
    login_page.abrir()
    
    # Intentar iniciar sesión con un usuario bloqueado en SauceDemo
    login_page.iniciar_sesion("locked_out_user", "secret_sauce")
    
    # Obtener el mensaje de error que muestra la plataforma
    mensaje_error = login_page.obtener_error()
    
    # Validar explícitamente que el sistema bloqueó el acceso con el mensaje correcto
    assert "Epic sadface: Sorry, this user has been locked out." in mensaje_error, \
        f"Error inesperado: Se obtuvo el mensaje -> '{mensaje_error}'"