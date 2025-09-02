# monotributo_simple.py
from dotenv            import dotenv_values
from funciones.navegar import default_firefox_options
from funciones.afip    import descargar_ultimo_vep_afip, login_afip, logout_afip, monotributo_simple_afip
from pathlib           import Path
from selenium          import webdriver

def liquidar_monotributo_simple() -> None:
    download_dir = str(Path.cwd() / "impuestos" / "vep_mono_simple")

    options = default_firefox_options(download_dir)
    # Login credentials
    config = dotenv_values()
    user = str(config.get('CUIT_MONO_SIMPLE'))
    password = str(config.get('PASSWORD_MONO_SIMPLE'))


    driver = webdriver.Firefox(options=options)
    driver = login_afip(driver, user, password)
    driver = monotributo_simple_afip(driver, pago="PMC")
    driver = descargar_ultimo_vep_afip(driver)
    driver = logout_afip(driver)
