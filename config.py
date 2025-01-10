import logging 
from dataclasses import dataclass

# PATHS
@dataclass
class Paths:
    
    DATA_PATH = "data"


@dataclass
class Const:
    # Количество старниц для сбора статей по поисковому запросу
    LIMIT_FOR_PAGE_PARSING = 10
    # Имя файла для сохранения страницы
    PAGE = "index.html"
    # Имя файла для сохранения заголовков страницы
    HEAD = "headers.json"
    
    ARCTICLES = "search_articles.md"

def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)40s:%(lineno)-4d %(levelname)-7s - %(message)s",
        # filename="legobase.log",
        # filemode="w",
    )
