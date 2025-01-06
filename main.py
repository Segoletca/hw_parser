import logging

from config import configure_logging
from Parser import Parser

log = logging.getLogger(__name__)

url = "https://habr.com/ru/companies/ruvds/articles/665084/"

parser = Parser(url)

def main():
    parser.res()



if __name__ == '__main__':
    configure_logging()
    log.info("Start program!")
    main()
