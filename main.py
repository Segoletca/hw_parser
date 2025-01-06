import logging

from config import configure_logging
from Searcher import Searcher


def main():
    log = logging.getLogger(__name__)
    log.info("Start program!")
    
    url = "https://habr.com/ru/search/"
    
    data = {
        "q": "http+как+устроен",
        "target_type": "posts",
        "order": "relevance",
        # "format": "json",
    }
    
    # url = "https://habr.com/ru/search/?q=http&target_type=posts&order=relevance"
    # url = "https://habr.com/ru/companies/ruvds/articles/665084/"
    
    searcher = Searcher(url, data)
    searcher.htmlParserAllPages()


if __name__ == '__main__':
    configure_logging()
    main()
