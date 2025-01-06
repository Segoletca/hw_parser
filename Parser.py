import requests as re
from logging import getLogger
import json
from config import Paths


log = getLogger(__name__)

"""_summary_
    - Общий метод для сохранения json `saveJson`
    - Метод для сохранения заголовков `saveHeader`
Raises:
    SystemExit: _description_
"""


class Parser:
    def __init__(self, url, data):
        self.savingObj = None
        self.fileName = None
        self.url = url
        self.base_url = url
        self.data = data
        self.page = re.get(self.url, self.data)
        if self.page.status_code == 404:
            log.warning("Ошибка get запроса!")
            log.error("Не найдено! Возможно URL указан неверно.")
            raise SystemExit
        # if page == re.models.Response
            
        self.headers = self.page.headers
        # self.test = self.page.json
   
   
    def getPageNoExept(self):
        self.page = re.get(self.url, self.data)
   
    def saveJson(self):
        # Needs: - fileName and savingObj
        with open(f"{Paths.DATA_PATH}/{self.fileName}", "w") as file:
            json.dump(self.savingObj, file, indent=4)

    def saveHeader(self):
        # In json format
        self.fileName = "raw_head_out.json"
        self.savingObj = dict(self.headers)
        
        self.saveJson()
        log.info(f"Файл {self.fileName} был сохранен.")
        
        self.fileName, self.savingObj = None, None
        
    def saveBody(self):
        self.fileName = "raw_body_out.json"
        self.savingObj = dict(self.page.text)
        
        self.saveJson()
        log.info(f"Файл {self.fileName} был сохранен.")
    
    # def res(self):
    #     # with open(f"{Paths.DATA_PATH}/raw_body_out.json", "w") as file:
    #     #     file.write(self.page.text)
    #     self.saveHeader()
    #     print()