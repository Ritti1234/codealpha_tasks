from  selenium  import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class infow():
    def __init__(self):
        option = webdriver.ChromeOptions()
        self.driver=webdriver.Chrome(options=option)
        self.driver.get("C:\ProgramData\Microsoft\Windows\Start Menu\Programs")
   
    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search=self.driver.find_element(By.XPATH,'/html/body/div[3]/form/fieldset/div/input')
        search.click()
        search.send_keys(query)
        enter =self.driver.find_element(By.XPATH,'/html/body/div[3]/form/fieldset/button')
        enter.click()



