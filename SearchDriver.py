from logging import getLogger
from config import Const, Paths
from Parser import Parser 
from bs4 import BeautifulSoup
import sys
from pathlib import Path



log = getLogger(__name__)


class SearchDriver(Parser):
    ## Небезопасный метод!!!
    def __handle_query(self):
        self.raw_query = sys.argv[1:]
        query = "+".join(self.raw_query)
        return query

    def response_by_query(self):
        query = {"q": f"{self.__handle_query()}"}
        query.update(self.data)
        self.data = query

        self.load_src()
        log.info(f"Used URL: {self.response.url}")
    
    def save_articles_link(self):
        with open(Path(Paths.DATA_PATH, Const.ARCTICLES), "w") as file:
            file.write(f'## Список статей по запросу "{" ".join(self.raw_query)}"\n\n')
            
            for title, link in self.articles_dict.items():
                file.write(f"- [{title}]({link})\n")
    
    def collect_articles(self):
        self.soup = BeautifulSoup(self.response.text, "lxml")
        # log.debug(self.soup.find("body").text)
        
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
            # log.debug(self.domen + block.get("href"))
            # for child in block.children:
            #     log.debug(child)


        # for block in blocks:
        #     post_title = 
        #     post_link
        #     log.debug(
        
        #     )
        # print(self.response.json())
    # def search(self):
    #     self.response_by_query()
        
    #     if not len(self.raw_query):
    #         log.error("Введите ключевые слова для запроса!")
    #         raise SystemExit
        
    #     self.collect_articles()


# class Searcher(Parser):
#     def htmlSearchOnePage(self):
#         self.bsoup = BeautifulSoup(self.response.text, 'html.parser')
#         # print(self.bsoup.title)
#         # print(self.bsoup)
#         # blocks = self.bsoup.find(attrs={"class": "tm-articles-list__item"})
#         blocks = self.bsoup.find_all(attrs={"data-test-id": "article-snippet-title-link"})
        
#         for element in blocks:
#             print(element.text)
        
#         # ids = self.bsoup.find_all(id=True)
#         # i = 0
#         # for element in ids:
#         #     id_value = element.get('data-test-id')
#         #     content = element.get_text()
        
#         #     if id_value == "articles-list-item":
#         #         print(f"ID: {id_value}")
#         #         print(f"Содержимое: {content}\n")
#         #         i += 1


#     def htmlSearchAllPages(self):
#         for page_num in range(1, Const.LIMIT_FOR_PAGE_PARSING):
#             self.url = self.base_url + f"page{page_num}"
#             self.getResponseNoExept()
#             if self.response.status_code != 200:
#                 break
            
#             self.htmlSearchOnePage()
#         log.info(f"Найдено {page_num} страниц")
        # elements = self.bsoup.find_all(id="specific_id")
        # for element in elements:
        #     content = element.get_text()
        #     print(content)
        
        # for resp in self.bsoup.find_all('a'):
            # print(resp.get("article-snippet-title-link"))
    