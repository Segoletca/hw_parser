from logging import getLogger
from config import Const
from Parser import Parser 
from bs4 import BeautifulSoup


log = getLogger(__name__)


class Searcher(Parser):
    def htmlSearchOnePage(self):
        self.bsoup = BeautifulSoup(self.page.text, 'html.parser')
        # print(self.bsoup.title)
        # print(self.bsoup)
        ids = self.bsoup.find_all(id=True)
        i = 0
        for element in ids:
            id_value = element.get('data-test-id')
            content = element.get_text()
            
            if id_value == "articles-list-item":
                print(f"ID: {id_value}")
                print(f"Содержимое: {content}\n")
                i += 1


    def htmlSearchAllPages(self):
        for page_num in range(1, Const.LIMIT_FOR_PAGE_PARSING):
            self.url = self.base_url + f"page{page_num}"
            self.getPageNoExept()
            if self.page.status_code != 200:
                break
            
            self.htmlParserOnePage()
            log.info(f"Найдено {page_num} страниц")
        
        # elements = self.bsoup.find_all(id="specific_id")
        # for element in elements:
        #     content = element.get_text()
        #     print(content)
        
        # for resp in self.bsoup.find_all('a'):
            # print(resp.get("article-snippet-title-link"))
    