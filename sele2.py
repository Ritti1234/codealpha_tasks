from  selenium  import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class music():
    def __init__ (self):
        option = webdriver.ChromeOptions()
        self.driver=webdriver.Chrome(options=option)
        self.driver.get("C:\ProgramData\Microsoft\Windows\Start Menu\Programs")


    def play(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query) 
        self.driver.implicitly_wait(3)   
        video=self.driver.find_element(By.XPATH,'//*[@id="video-title"]')
        video.click()

        wait=WebDriverWait(self.driver,10)
        while True:
            try:
                print("Waiting for video to finish..")
                wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-image/img")))
                break
            except:
                pass

        


