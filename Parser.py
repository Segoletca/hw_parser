import requests as req
from logging import getLogger
import json
from config import Paths, Const
from pathlib import Path
from bs4 import BeautifulSoup


log = getLogger(__name__)

"""_summary_
    - Метод для предварительного сохранения страницы `load_src`

Raises:
    SystemExit: _description_
"""


class Parser:
    def __init__(self, url, domen=None, data=None, headers=None):
        self.domen = domen
        self.url = url
        self.data = data
        self.headers = headers
    
    # Метод для создания объекта с ответом от сайта
    def load_src(self):
        self.response = req.get(self.url, params=self.data, headers=self.headers)
        if not self.response.ok:
            log.warning("Ошибка get запроса!")
            log.error("Не найдено! Возможно URL указан неверно.")
            raise SystemExit
        
        self.used_url = self.response.url
        self.used_headers = self.response.headers
        
        with open(Path(Paths.DATA_PATH, Const.PAGE), "w", encoding="utf-8") as file:
            file.write(self.response.text)
        
        with open(Path(Paths.DATA_PATH, Const.HEAD), "w", encoding="utf-8") as file:
            json.dump(dict(self.response.headers), file, indent=4)
    
    def beautiful_soup(self):
        with open(Const.PAGE) as file:
            src = file.read()
        
        self.soup = BeautifulSoup(src, "lxml")
