import logging

from config import configure_logging
from Searcher import Searcher
import time

log = logging.getLogger(__name__)

def main():
    log.info("Start program!")
    
    url = "https://habr.com/ru/search/"
    # url = "https://api.github.com"
    # url = "https://habr.com/ru/companies/qrator/articles/416633/"
    
    domen = "https://habr.com"
    
    headers = {"user-agent": "UserHostName"}
    
    data = {
        # "q": "http",
        "target_type": "posts",
        "order": "relevance",
        # "format": "json",
    }

    
    searcher = Searcher(url, domen, data, headers) # Создаем объект парсера
    
    searcher.search() # Метод для поиска статей c запросом из командной строки
    searcher.get_all_articles() # Аналог `.search()`, но парсит первые N страниц 
    
    # searcher.save_articles_link()




if __name__ == '__main__':
    configure_logging()
    start_time = time.time()
    main()
    log.info(f"Время выполнения - {round(time.time() - start_time, 2)} сек")
