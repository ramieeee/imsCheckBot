from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import getpass
from bs4 import BeautifulSoup
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
        # time.sleep(3)
    
    def waiting_time(self):
        return random.randint(1, 3) / 10
        
    def log_in(self):
        # login id, pw input field Xpath
        id = input('id: ')
        pw = getpass.getpass('pw: ')

        id_path = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/input'
        pw_path = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/input'
        id_input = self.driver.find_element(by=By.XPATH, value=id_path)
        pw_input = self.driver.find_element(by=By.XPATH, value=pw_path)
        login_button = self.driver.find_element(by=By.XPATH, value='/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td[3]/input')

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

    # def check_num_error(self):
    #     error_msg_path = '/html/body/div[1]/table/tbody/tr/td[2]/span[2]'
    #     error_msg = self.driver.find_element(by=By.XPATH, value=error_msg_path).text
    #     if error_msg:
    #         return 1
    #     else:
    #         return 0

    def find_ims(self, num):
        # url = f'https://ims.tmaxsoft.com/tody/ims/issue/issueView.do?issueId={num}'
        # html = requests.get(url, headers=self.header).text
        with open('sample.txt', 'r') as f:
            html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            findall = soup.find_all('p')
            print(findall)

        # ims_num_input_path = '/html/body/div[1]/table/tbody/tr/td[2]/span[1]/input'
        # ims_num_input = self.driver.find_element(by=By.XPATH, value=ims_num_input_path)
        # ims_num_input.click()
        # time.sleep(self.waiting_time())
        # ims_num_input.clear()
        # time.sleep(self.waiting_time())
        # ims_num_input.send_keys(num)
        # time.sleep(self.waiting_time())
        # ims_num_input.send_keys(Keys.ENTER)
        # time.sleep(2)
    
    def issue_details(self):
        action_log_path = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[7]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[3]/span'
        action_log = self.driver.find_element(by=By.XPATH, value=action_log_path).text
        print(action_log)

        latest_log_info_path = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[7]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[1]/div[1]/span[1]'
        latest_log_info = self.driver.find_element(by=By.XPATH, value=latest_log_info_path).text
        print(latest_log_info)
        
        latest_log_text_path = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[7]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[1]/div[2]/div/p[1]'
        latest_log_text = self.driver.find_element(by=By.XPATH, value=latest_log_text_path).text
        print(latest_log_text)



ims_check_bot = IMSCheckBot()
# ims_check_bot.log_in()
ims_check_bot.find_ims(279541)
