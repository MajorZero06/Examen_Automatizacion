from selenium import webdriver

# Clase que configura las opciones del navegador Chrome
class BrowserConfig:
    @staticmethod
    def get_chrome_options():
        # Crea un objeto de opciones de Chrome
        chrome_options = webdriver.ChromeOptions()
        
        # Executes Chrome en modo headless (sin interfaz gráfica)
        chrome_options.add_argument('--headless')
        
        # Reduce el uso compartido de memoria para evitar errores en sistemas limitados
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        # Deshabilita la aceleración de hardware en GPU
        chrome_options.add_argument('--disable-gpu')
        
        # Habilita el uso de SwiftShader, un emulador de GPU
        chrome_options.add_argument('--enable-unsafe-swiftshader')

        # Desactivar la carga de imágenes
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        
        # Devuelve el objeto de opciones configurado
        return chrome_options