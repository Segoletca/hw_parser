from logging import getLogger
from config import Const, Paths
from Parser import Parser 
from bs4 import BeautifulSoup
import sys
from pathlib import Path



log = getLogger(__name__)


class SearchDriver(Parser):
    ## Небезопасный метод!!!
    def handle_query(self):
        self.raw_query = sys.argv[1:]
        
        if not len(self.raw_query):
            log.error("Введите ключевые слова для запроса!")
            raise SystemExit
        
        query = "+".join(self.raw_query)
        return query

    def response_by_query(self):
        query = {"q": f"{self.handle_query()}"}
        query.update(self.data)
        self.data = query

        self.load_src()
        log.debug(f"Сообщение из response_by_query, url: {self.response.url}")
        log.info(f"Used URL: {self.response.url}")
    
    
    
    def create_file_for_articles_link(self):
        with open(Path(Paths.DATA_PATH, Const.ARCTICLES), "w") as file:
            file.write(f'## Список статей по запросу "{" ".join(self.raw_query)}"\n\n')
    
    def save_articles_link(self):
        with open(Path(Paths.DATA_PATH, Const.ARCTICLES), "a") as file:
            # file.write(f'## Список статей по запросу "{" ".join(self.raw_query)}"\n\n')
            for title, link in self.articles_dict.items():
                file.write(f"- [{title}]({link})\n")
    
    def save_md_file(self):
        self.create_file_for_articles_link()
        self.save_articles_link()
    
    
    # Парсит поисковый запрос забирая названия найденных статей и ссылки сохраняя в `self.articles_dict`
    def collect_articles(self, **kwargs):
        if "response_txt" in kwargs.keys():
            response_txt = kwargs["response_txt"]
        else:
            response_txt = self.response.text
        
        self.soup = BeautifulSoup(response_txt, "lxml")
        
        with open(Path(Paths.DATA_PATH, Const.PAGE), "w", encoding="utf-8") as file:
            file.write(str(self.soup))

        blocks = self.soup.find_all(class_="tm-title__link")
        
        if not len(blocks):
            log.warning('Не было обнаружено ни одного элемента класса "tm-title__link"')
        
        self.articles_dict = dict()
        for block in blocks:
            article_dict = {
                block.text: self.domen + block.get("href")
            }
            self.articles_dict.update(article_dict)
        
        log.debug(f"Найдено {len(self.articles_dict)} статей на странице")
