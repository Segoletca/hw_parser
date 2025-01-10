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
    
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
    
    data = {
        # "q": "http",
        "target_type": "posts",
        "order": "relevance",
        # "format": "json",
    }

    # Parser(url).load_src()
    
    searcher = Searcher(url, domen, data, headers)
    searcher.search()
    
    searcher.get_all_articles()
    
    # searcher.save_articles_link()




if __name__ == '__main__':
    configure_logging()
    start_time = time.time()
    main()
    log.info(f"Время выполнения - {round(time.time() - start_time, 2)} сек")
