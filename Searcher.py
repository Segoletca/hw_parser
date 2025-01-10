from logging import getLogger
from SearchDriver import SearchDriver
from config import Const

log = getLogger(__name__)

class Searcher(SearchDriver):
    def search(self):
        self.response_by_query()
        
        if not len(self.raw_query):
            log.error("Введите ключевые слова для запроса!")
            raise SystemExit
        
        self.collect_articles()
    
    # def get_all_articles_async(self):
    def get_all_articles(self):
        # print(self.url)
        # print(self.raw_query)
        # print(self.data)
        # print(self.domen)
        
        for page_num in range(1, Const.LIMIT_FOR_PAGE_PARSING):
            self.url_with_page = self.url + f"page{page_num}"
            self.


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