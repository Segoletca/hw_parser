import requests as re


class Parser:
    def __init__(self, url):
        self.url = url
        self.page = re.get(self.url)
        self.headers = self.page.headers
        # self.test = self.page.json
        
    def res(self):
        # print(self.headers)
        print(self.headers)
