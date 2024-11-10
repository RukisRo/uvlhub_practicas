import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# Configurar Selenium para usar Chromium
options = webdriver.ChromeOptions()

# Quita '--headless' para ejecutar el navegador de manera visible
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Iniciar el driver de Chromium usando webdriver-manager
service = Service(ChromeDriverManager().install())
# Si obtienes un error al lanzar la prueba, puedes probar a cambiar la línea anterior por la siguiente
# service = Service('/usr/bin/chromedriver')  # Pero tendrás que cerciorarte de la ruta exacta al driver en tu equipo

driver = webdriver.Chrome(service=service, options=options)

try:
    # 1. Abrir Proyecto
    driver.get("http://localhost:5000/login")
    time.sleep(2)
    # 2. Logear
    driver.set_window_size(912, 1011)
    driver.find_element(By.ID, "email").click()
    driver.find_element(By.ID, "email").send_keys("user1@example.com")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    # 3.Crear un notepad 
    driver.get("http://localhost:5000/notepad/create")
    driver.find_element(By.ID, "title").click()
    driver.find_element(By.ID, "title").send_keys("NoteBook creado con Selenium")
    driver.find_element(By.ID, "body").click()
    driver.find_element(By.ID, "body").send_keys("descripcion")
    driver.find_element(By.ID, "submit").click()



except Exception as e:
    print(f"Error: {e}")
    driver.save_screenshot("error_screenshot.png")
    print("Captura de pantalla guardada como 'error_screenshot.png'")

#finally:
    # Cerrar el navegador
    #driver.quit()