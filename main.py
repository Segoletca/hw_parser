import logging

from config import configure_logging
from Searcher import Searcher


def main():
    log = logging.getLogger(__name__)
    log.info("Start program!")
    
    url = "https://habr.com/ru/search/"
    # url = "https://api.github.com"
    # url = "https://habr.com/ru/companies/qrator/articles/416633/"
    
    domen = "https://habr.com"
    
    header = {"user-agent": "user"}
    
    data = {
        # "q": "http",
        "target_type": "posts",
        "order": "relevance",
        # "format": "json",
    }

    # Parser(url).load_src()
    
    searcher = Searcher(url, domen, data)
    searcher.search()
    searcher.get_all_articles()
    
    # searcher.save_articles_link()




if __name__ == '__main__':
    configure_logging()
    main()
