import time
from datetime                             import date
from dateutil.relativedelta               import relativedelta
from dotenv                               import dotenv_values
from funciones                            import boton
from pathlib                              import Path
from selenium                             import webdriver
from selenium.webdriver.common.by         import By
from selenium.webdriver.firefox.options   import Options


def deducciones_misiones(mes_anterior=True):
    # Download directory
    download_dir = str(Path.cwd() / "deducciones" / "misiones")

    # Browser options
    options = Options()
    options.set_preference("geo.enabled", False)
    options.set_preference("browser.download.folderList", 2) # 2 = custom
    options.set_preference("browser.download.dir", download_dir)

    # Login credentials
    config = dotenv_values()
    user = str(config.get('CUIT_MISIONES'))
    password = str(config.get('PASSWORD_MISIONES'))

    # Execution
    driver = webdriver.Firefox(options=options)
    driver.get('https://extranet.atmisiones.gob.ar/Extranet/index.php')

    login_btn = boton(driver, (By.ID, "btn_sit"))
    login_btn.click()

    user_btn = boton(driver, (By.ID, "log_user_aux"))
    user_btn.send_keys(user)
    password_btn = boton(driver, (By.ID, "log_pass_aux"))
    password_btn.send_keys(password)
    ingresar_btn = boton(driver, (By.ID, "btn_ingresar"))
    ingresar_btn.click()

    input("Resolver el captcha y ENTER para continuar")

    iibb_btn = boton(driver, (By.XPATH, "//a[.//span[text()='Ingresos Brutos']]"))
    iibb_btn.click()
    ret_perc_btn = boton(driver, (By.XPATH, "//a[.//span[text()='Consulta de Ret./Perc.']]"))
    ret_perc_btn.click()

    desde_btn = boton(driver, (By.ID, "periodo_desde"))
    hasta_btn = boton(driver, (By.ID, "periodo_hasta"))
    if mes_anterior:
        month_input = (date.today() - relativedelta(months=1)).strftime("%Y/%m")
        desde_btn.send_keys(month_input)    
        hasta_btn.send_keys(month_input)
    else:
        desde_input = input("Desde (aaaa/mm): ")
        hasta_input = input("Hasta (aaaa/mm): ")
        desde_btn.send_keys(desde_input)    
        hasta_btn.send_keys(hasta_input)
    
    descargar_btn = boton(driver, (By.ID, "btn_excel"))
    descargar_btn.click()
    time.sleep(1)


    logout_btn = boton(driver, (By.XPATH, "//a[@onclick='salir();']"))
    logout_btn.click()

    driver.quit()

