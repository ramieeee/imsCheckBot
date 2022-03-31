from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import getpass
import requests

class IMSCheckBot:
    def __init__(self):
        # driver setting
        self.options = Options()
        self.options.add_argument("headless")
        self.options.add_argument("--window-size=1024,768")
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=self.options)
        self.url = "https://ims.tmaxsoft.com/"
        self.driver.get(self.url)
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
        time.sleep(3)
    
    def waiting_time(self):
        return random.randint(1, 3) / 10
        
    def log_in(self):
        # login id, pw input field Xpath
        id = input('id: ')
        pw = getpass.getpass('pw: ')

        id_path = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/input'
        pw_path = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/input'
        login_button_path = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td[3]/input'
        id_input = self.driver.find_element(by=By.XPATH, value=id_path)
        pw_input = self.driver.find_element(by=By.XPATH, value=pw_path)
        login_button = self.driver.find_element(by=By.XPATH, value=login_button_path)

        # id input
        id_input.click()
        time.sleep(self.waiting_time())
        id_input.clear()
        time.sleep(self.waiting_time())
        id_input.send_keys(id)
        time.sleep(1)
        
        # pw input
        pw_input.click()
        time.sleep(self.waiting_time())
        pw_input.clear()
        time.sleep(self.waiting_time())
        pw_input.send_keys(pw)
        time.sleep(0.5)

        login_button.click()

    def get_ims_info(self, num):
        url = f'https://ims.tmaxsoft.com/tody/ims/issue/issueView.do?issueId={num}'

        # check HTTP status
        # html = requests.get(url, headers=self.header)
        # print(f'*********{html.status_code}********')

        # if html.status_code != 200:
        #     print(f'Page error. Error code {html.status_code}')
        #     return
        self.driver.get(url)
        time.sleep(2)

        try:
            error_check_path = '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/pre/span'
            if self.driver.find_element(by=By.XPATH, value=error_check_path).text:
                print('\nSystem: Invalid IMS number')
                return 0, 0, 0
        except:
            pass

        try:
        # ims_title
            ims_title_path = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr/td[2]'
            ims_title = self.driver.find_element(by=By.XPATH, value=ims_title_path).text.strip()

        # date check
            ims_date_path = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[3]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table[2]/tbody/tr/td[1]/table/tbody/tr[20]/td[2]'

            ims_date = self.driver.find_element(by=By.XPATH, value=ims_date_path).text.strip()
            return int(num), ims_title, ims_date

        except:
            pass