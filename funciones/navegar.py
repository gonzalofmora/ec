# navegar.py
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options   import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support           import expected_conditions as EC
from selenium.webdriver.support.ui        import WebDriverWait

def boton(driver: WebDriver, tuple: tuple[str, str]) -> WebElement : 
    by_type, text = tuple
    btn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((by_type, text))
    )
    return btn

def default_firefox_options(downloads_dir : str) -> Options :
    # Browser options
    options = Options()
    options.set_preference("browser.download.folderList", 2) # custom folder
    options.set_preference("browser.download.dir", downloads_dir)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    options.set_preference("pdfjs.disabled", True)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    return options
