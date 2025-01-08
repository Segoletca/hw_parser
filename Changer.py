from Parser import Parser
from bs4 import BeautifulSoup

class HeaderChanger(Parser):
    # def __init__(self, headers):
    #     super().__init__()
    #     self.headers = headers
    #     print(self.headers)
    #     print(self.url)

    def current_status(self):
        bsoup = BeautifulSoup(self.response.text, "html.parser")
        
        print(self.headers)
