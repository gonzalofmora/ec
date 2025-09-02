from selenium.webdriver.support           import expected_conditions as EC
from selenium.webdriver.support.ui        import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver

def boton(driver: WebDriver, tuple: tuple[str, str]):
    by_type, text = tuple
    btn = WebDriverWait(driver, 10).until(
        EC.visibility_of(driver.find_element(by_type, text))
    )
    return btn