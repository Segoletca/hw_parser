from logging import getLogger
from SearchDriver import SearchDriver
from config import Const, Paths
from pathlib import Path
import requests as req

log = getLogger(__name__)

class Searcher(SearchDriver):
    # Метод для запроса на поиск статей из командной строки (первые 20 статей) с записью в файл data/search_aritcles.md
    def search(self):
        self.response_by_query()
                
        self.collect_articles()
    
    # Повтоярет поведение `search`, только сохраняет первые 90 статей (9 страниц)
    def get_all_articles(self):
        
        self.test_collect_all_page = dict()
        
        
        for page_num in range(1, Const.LIMIT_FOR_PAGE_PARSING):
            self.url_with_page = self.url + f"page{page_num}"
            
            query = {"q": f"{self.handle_query()}"}
            query.update(self.data)
            data = query
            
            response = req.get(self.url_with_page, params=data, headers=self.headers)
            
            self.collect_articles(response_txt=response.text)
            self.test_collect_all_page.update(self.articles_dict)
        self.articles_dict = dict()
        self.articles_dict.update(self.test_collect_all_page)
        
        
        # Save
        self.create_file_for_articles_link()
        # with open(Path(Paths.DATA_PATH, Const.ARCTICLES), "a") as file:
        #     file.write(f'\n## Страница {page_num}\n')
        self.save_articles_link()
        log.debug(self.response.url)
