from Parser import Parser 
from config import Paths
from bs4 import BeautifulSoup

class TestPars(Parser):
    def test_write(self):
        with open(f"{Paths.DATA_PATH}/test.html", "w", encoding="utf-8") as file:
            file.write(self.response.text)
            
    def pars(self):
        soup = BeautifulSoup(self.response.text, "html.parser")
        
        block = soup.find("div", attrs={"data-test-id": "articleHubsList"})
        
        elements = block.find_all("a", attrs={"class": "tm-publication-hub__link"})
        
        for element in elements:
            print(element.text)
    
