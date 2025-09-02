# afip.py
import time
from funciones.navegar                              import boton
from selenium.webdriver                   import Keys
from selenium.webdriver.common.by         import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support           import expected_conditions as EC
from selenium.webdriver.support.ui        import WebDriverWait

def buscador_afip(driver: WebDriver, aplicativo: str) -> WebDriver:
    buscador_btn = boton(driver, (By.ID, "buscadorInput"))
    buscador_btn.clear()
    buscador_btn.send_keys(aplicativo)
    buscador_btn.send_keys(Keys.ARROW_DOWN)
    buscador_btn.send_keys(Keys.ENTER)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    return driver

def descargar_ultimo_vep_afip(driver: WebDriver) -> WebDriver :
    driver = buscador_afip(driver, "Presentación de DDJJ y Pagos")
    aceptar_btn = boton(driver, (By.XPATH, "//button[@title='Aceptar']"))
    aceptar_btn.click()
    consulta_btn = boton(driver, (By.XPATH, "(//span[contains(., 'Consulta')])[4]"))
    driver.execute_script("arguments[0].click();", consulta_btn)
    ver_consulta_btn = boton(driver, (By.XPATH, "//button[contains(., 'Ver consulta')]"))
    ver_consulta_btn.click()
    exportar_pdf = boton(driver, (By.XPATH, "//a[@title='Exportar detalle en archivo PDF']"))
    driver.execute_script("arguments[0].click();", exportar_pdf)
    time.sleep(1)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return driver

def login_afip(driver: WebDriver, user: str, password: str) -> WebDriver:
    driver.get("https://auth.afip.gob.ar/contribuyente_/login.xhtml")
    user_login_btn = boton(driver, (By.ID, "F1:username"))
    user_login_btn.clear()
    user_login_btn.send_keys(user)
    siguiente_btn = boton(driver, (By.ID, "F1:btnSiguiente"))
    siguiente_btn.click()
    password_login_btn = boton(driver, (By.ID, "F1:password"))
    password_login_btn.clear()
    password_login_btn.send_keys(password)
    ingresar_btn = boton(driver, (By.ID, "F1:btnIngresar"))
    ingresar_btn.click()
    return driver

def logout_afip(driver: WebDriver) -> WebDriver :
    logout_btn = boton(driver, (By.ID, "userIconoChico"))
    logout_btn.click()
    cerrar_sesion = boton(driver, (By.XPATH, "//*[normalize-space(text())='Cerrar sesión']"))
    cerrar_sesion.click()
    return driver

def monotributo_simple_afip(driver: WebDriver, pago:str="PMC") -> WebDriver:
    driver = buscador_afip(driver, 'Monotributo ad')
    pagar_btn = boton(driver, (By.XPATH, "//a[@href='PPV_online.aspx']"))
    pagar_btn.click()

    iframe = boton(driver, (By.TAG_NAME, "iframe"))
    driver.switch_to.frame(iframe)

    medios_de_pago = {
        "PMC" : "1002", # Pago Mis Cuentas
    }
    for attempt in range(3):
        try:
            pmc_btn = boton(driver, (By.XPATH, f"//div[@data-value='{medios_de_pago[pago]}']"))
            pmc_btn.click()
            generar_btn = boton(driver, (By.XPATH, "//input[@value='GENERAR VOLANTE DE PAGO']"))
            generar_btn.click()
            break
        except Exception:
            if attempt == 2:
                raise Exception("No hay tal objeto después de 3 intentos")
    time.sleep(3)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return driver
