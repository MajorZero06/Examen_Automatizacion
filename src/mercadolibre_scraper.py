from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from .browser_config import BrowserConfig

# Inicializa la clase que configura el navegador
class WebScraper:
    def __init__(self, base_url):
        # Obtiene las opciones de Chrome desde BrowserConfig
        chrome_options = BrowserConfig.get_chrome_options()
        # Inicializa el navegador Chrome con las opciones especificadas
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.base_url = base_url  # Establece la URL base para el scraper

    # Abre una URL especifica que sera proporcionada por la clase hija (scraper)
    def open_url(self, url):
        self.driver.get(url)

    # Cierra el navegador
    def close(self):
        self.driver.quit()

# Clase que hereda de WebScraper y añade funcionalidad específica para MercadoLibre
class scraper(WebScraper):
    def __init__(self):
        # Inicializa la clase base con la URL de MercadoLibre
        super().__init__('https://www.mercadolibre.com')

    # Navega a la página de México en MercadoLibre
    def navigate_to_mexico(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "México")]'))
        )
        mexico_link = self.driver.find_element(By.XPATH, '//a[contains(text(), "México")]')
        mexico_link.click()

    # Busca un producto específico en la barra de búsqueda
    def search_product(self, product_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input.nav-search-input#cb1-edit'))
        )
        search_box = self.driver.find_element(By.CSS_SELECTOR, 'input.nav-search-input#cb1-edit')
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)

    # Aplica filtros de búsqueda en la página
    def apply_filters(self):
        # Filtro "Nuevo"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Nuevo']/ancestor::a[@class='ui-search-link']"))
        )
        filter_link = self.driver.find_element(By.XPATH, "//span[text()='Nuevo']/ancestor::a[@class='ui-search-link']")
        href = filter_link.get_attribute('href')
        self.driver.get(href)

        # Filtro "Distrito Federal"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Distrito Federal']/ancestor::a[@class='ui-search-link']"))
        )
        filter_link = self.driver.find_element(By.XPATH, "//span[text()='Distrito Federal']/ancestor::a[@class='ui-search-link']")
        href = filter_link.get_attribute('href')
        self.driver.get(href)

        # Filtro "Mayor precio"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.andes-dropdown__standalone-arrow'))
        )
        arrow_button = self.driver.find_element(By.CSS_SELECTOR, 'div.andes-dropdown__standalone-arrow')
        arrow_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'li.andes-list__item[data-key="price_desc"] span.andes-list__item-primary'))
        )
        highest_price_option = self.driver.find_element(By.CSS_SELECTOR, 'li.andes-list__item[data-key="price_desc"] span.andes-list__item-primary')
        highest_price_option.click()

    # Obtiene los resultados de la búsqueda, incluyendo títulos y precios de productos
    def get_results(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'ui-search-layout__item')]"))
        )
        product_titles = self.driver.find_elements(By.CSS_SELECTOR, 'a.poly-component__title')[:5]
        product_prices = self.driver.find_elements(By.CSS_SELECTOR, 'div.poly-price__current span.andes-money-amount__fraction')[:5]

        # Construye la lista de resultados
        results = []
        for title, price in zip(product_titles, product_prices):
            results.append((title.text, price.text))
        return results