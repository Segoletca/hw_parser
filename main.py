import logging

from config import configure_logging
from Searcher import Searcher
from Changer import HeaderChanger
from test import TestPars


def main():
    log = logging.getLogger(__name__)
    log.info("Start program!")
    
    url = "https://habr.com/ru/search/"
    
    header = {"user-agent": "user"}
    
    data = {
        "q": "http+как+устроен",
        "target_type": "posts",
        "order": "relevance",
        # "format": "json",
    }
    # url = "https://habr.com/ru/companies/ruvds/articles/342346/"
    # data = None
    # url = "https://habr.com/ru/search/?q=http&target_type=posts&order=relevance"
    # url = "https://habr.com/ru/companies/ruvds/articles/665084/"
    
    # searcher = Searcher(url, data)
    # searcher.htmlSearchOnePage()
    # searcher.htmlSearchAllPages()
    # TestPars(url, data).pars()
    
    
    changer = HeaderChanger(url, data)
    
    changer.current_status()
    


if __name__ == '__main__':
    configure_logging()
    main()
