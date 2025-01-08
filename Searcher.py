from logging import getLogger
from config import Const
from Parser import Parser 
from bs4 import BeautifulSoup


log = getLogger(__name__)


class Searcher(Parser):
    def htmlSearchOnePage(self):
        self.bsoup = BeautifulSoup(self.response.text, 'html.parser')
        # print(self.bsoup.title)
        # print(self.bsoup)
        # blocks = self.bsoup.find(attrs={"class": "tm-articles-list__item"})
        blocks = self.bsoup.find_all(attrs={"data-test-id": "article-snippet-title-link"})
        
        for element in blocks:
            print(element.text)
        
        # ids = self.bsoup.find_all(id=True)
        # i = 0
        # for element in ids:
        #     id_value = element.get('data-test-id')
        #     content = element.get_text()
        
        #     if id_value == "articles-list-item":
        #         print(f"ID: {id_value}")
        #         print(f"Содержимое: {content}\n")
        #         i += 1


    def htmlSearchAllPages(self):
        for page_num in range(1, Const.LIMIT_FOR_PAGE_PARSING):
            self.url = self.base_url + f"page{page_num}"
            self.getResponseNoExept()
            if self.response.status_code != 200:
                break
            
            self.htmlSearchOnePage()
        log.info(f"Найдено {page_num} страниц")
        # elements = self.bsoup.find_all(id="specific_id")
        # for element in elements:
        #     content = element.get_text()
        #     print(content)
        
        # for resp in self.bsoup.find_all('a'):
            # print(resp.get("article-snippet-title-link"))
    