import os
import re

import pytest
from selenium import webdriver


@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Guarda el resultado de cada fase (setup, call, teardown) dentro del test
    # para que la fixture pueda saber, al terminar, si pasó o falló.
    reporte = yield
    setattr(item, f"rep_{reporte.when}", reporte)
    return reporte


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # Selenium Manager (incluido desde Selenium 4.6) resuelve el driver solo.
    driver = webdriver.Chrome(options=options)

    yield driver

    # --- BLOQUE DE EVIDENCIA AUTOMÁTICA ---
    try:
        os.makedirs("evidence", exist_ok=True)
        reporte = getattr(request.node, "rep_call", None)
        resultado = reporte.outcome.upper() if reporte else "SIN_RESULTADO"
        nombre = re.sub(r"[^\w\-]", "_", request.node.name)
        ruta = f"evidence/{nombre}_{resultado}.png"
        driver.save_screenshot(ruta)
        print(f"\n[EVIDENCIA] Captura guardada en: {ruta}")
    finally:
        driver.quit()