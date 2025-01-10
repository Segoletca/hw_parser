from logging import getLogger
from SearchDriver import SearchDriver
from config import Const, Paths
from pathlib import Path
import requests as req
import asyncio

log = getLogger(__name__)

class Searcher(SearchDriver):
    def search(self):
        self.response_by_query()
                
        self.collect_articles()
    
    # def get_all_articles_async(self):
    def get_all_articles(self):
        
        
        self.test_collect_all_page = dict()
        
        
        
        for page_num in range(1, 10): # Const.LIMIT_FOR_PAGE_PARSING
            self.url_with_page = self.url + f"page{page_num}"
            
            query = {"q": f"{self.handle_query()}"}
            query.update(self.data)
            data = query
            
            response = req.get(self.url_with_page, params=data, headers=self.headers)
            
            self.collect_articles(response_txt=response.text)
            self.test_collect_all_page.update(self.articles_dict)
        self.articles_dict = dict()
        self.articles_dict.update(self.test_collect_all_page)
        # log.debug(f"From all page: {self.articles_dict}")
        # self.response_by_query()

        
        # Save
        self.create_file_for_articles_link()
        with open(Path(Paths.DATA_PATH, Const.ARCTICLES), "a") as file:
            file.write(f'\n## Страница {page_num}\n')
        self.save_articles_link()
        log.debug(self.response.url)
        # print(self.url_with_page)
        
        # print(self.url)
            











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