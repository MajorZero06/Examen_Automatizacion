from src.mercadolibre_scraper import scraper  # Importa la clase scraper desde el módulo mercadolibre_scraper en src

if __name__ == "__main__":
    scraper = scraper()  # Crea una instancia de la clase scraper
    scraper.open_url(scraper.base_url)  # Abre la URL base (https://www.mercadolibre.com)
    scraper.navigate_to_mexico()  # Navega a la página de México en MercadoLibre
    scraper.search_product('playstation5')  # Busca el producto "playstation5" en la página
    scraper.apply_filters()  # Aplica los filtros de búsqueda especificados
    results = scraper.get_results()  # Obtiene los resultados de la búsqueda

    # Itera sobre los resultados y los imprime en formato "n. Producto: title - Precio: price"
    for n, (title, price) in enumerate(results, start=1):
        print(f'{n}. Producto: {title} - Precio: {price}')
    
    scraper.close()  # Cierra el navegador al finalizar