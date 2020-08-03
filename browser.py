import re

import time
import os

from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
load_dotenv()

class VideoBroswer:

    def __init__(self, url):
        try :
            self.driver = webdriver.Chrome(seleniumwire_options={'connection_timeout': None})
            self.url = url
            if not self.visit_page():
                self.wait_for_login()
            self.saveCookie()
            self.getVideos()
        finally:
            self.driver.quit()
        

    def visit_page(self):
        self.driver.get(self.url)
        return self.landed()

    def wait_for_login(self):
        if re.search('login', self.driver.title, re.IGNORECASE):
            self.login()
        else:
            WebDriverWait(self.driver, 300).until(EC.url_matches(self.url))

    def login(self):
        self.driver.find_element_by_css_selector('#username').send_keys(os.getenv('USERNAME'))
        self.driver.find_element_by_css_selector('#password').send_keys(os.getenv('PASSWORD'))
        self.driver.find_element_by_css_selector('#loginBtn').click()
        pass

    def landed(self):
        return self.driver.current_url == self.url

    def saveCookie(self):
        try:
            element = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.ID, "agree_button"))
            )
            element.click()
        finally:
            pass

    def getVideos(self):
        elements = self.driver.find_elements_by_css_selector('iframe')
        for element in elements:
            self.driver.switch_to.frame(element)
            self.activateVideo()
            self.driver.switch_to.default_content()
        time.sleep(5)
        for request in driver.requests:
            if request.response and re.search('index', request.url, re.IGNORECASE):
                print(request.url, request.response.status_code)
        time.sleep(60)

    def activateVideo(self):
        try:
            print(self.driver.find_element_by_css_selector('#copyrightNoticeContainer').get_attribute('style'))
            WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((By.ID, "copyrightNoticeContainer")))
            element = WebDriverWait(self.driver, 120).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#player > div.fp-player > div.fp-ui"))
            )
            element.click()
            request = self.driver.wait_for_request('.+/index.m3u8', timeout=60)
            print(request.url)
        finally:
            pass
        

if __name__ == '__main__':
    x = VideoBroswer(os.get_env('URL'))