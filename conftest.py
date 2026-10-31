import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver
    
    # --- BLOQUE DE EVIDENCIA AUTOMÁTICA ---
    # Crear carpeta de evidencias si no existe
    os.makedirs("evidence", exist_ok=True)
    
    # Tomar captura de pantalla al finalizar la prueba
    test_name = request.node.name
    screenshot_path = f"evidence/{test_name}.png"
    driver.save_screenshot(screenshot_path)
    print(f"\n[EVIDENCIA] Captura guardada en: {screenshot_path}")
    
    driver.quit()