import logging
from config import configure_logging

log = logging.getLogger(__name__)


def main():
    print("Hello")


if __name__ == '__main__':
    configure_logging()
    log.warning("Start program!")
    main()
