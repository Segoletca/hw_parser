import logging

from config import configure_logging
from Parser import Parser


def main():
    log = logging.getLogger(__name__)
    log.info("Start program!")
    
    url = "https://habr.com/ru/companies/ruvds/articles/665084/"
    
    parser = Parser(url)
    parser.res()
    
    # parser.saveHeader()



if __name__ == '__main__':
    configure_logging()
    main()
