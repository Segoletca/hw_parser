import logging

from config import configure_logging
from Searcher import Searcher
from Changer import HeaderChanger
from test import TestPars
from Parser import Parser


def main():
    log = logging.getLogger(__name__)
    log.info("Start program!")
    
    # url = "https://habr.com/ru/search/"
    url = "https://api.github.com"
    # url = "https://habr.com/ru/companies/qrator/articles/416633/"
    
    header = {"user-agent": "user"}
    
    data = {
        # "q": "http",
        "target_type": "posts",
        "order": "relevance",
        # "format": "json",
    }

    # Parser(url).load_src()
    
    Searcher(url, data).post_list_by_query()
    




if __name__ == '__main__':
    configure_logging()
    main()
