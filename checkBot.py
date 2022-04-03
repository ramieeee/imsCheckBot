from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import getpass
from bs4 import BeautifulSoup
import time


class IMSCheckBot:
    def __init__(self):
        # driver setting
        self.options = Options()
        self.options.add_argument("headless")
        self.options.add_argument("--window-size=1024,768")
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=self.options)
        self.url = "https://ims.tmaxsoft.com/"
        # self.driver.get(self.url)
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
        time.sleep(3)
    
    def waiting_time(self):
        return random.randint(1, 3) / 10
        
    def log_in(self):
        self.driver.get(self.url)
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

    def login_check(self):
        try:
            login_error_path = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td'
            login_error = self.driver.find_element(By.XPATH, value=login_error_path).text
        
            if login_error == '* User password miss matched':
                return 0
        except:
            return 1

    def get_details(self, num):
        url = f'https://ims.tmaxsoft.com/tody/ims/issue/issueView.do?issueId={num}'
        self.driver.get(url)
        time.sleep(1)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        body_list = soup.find_all('div', {'id': 'IssueDescriptionDiv'})
        body_temp = []
        for i in body_list:
            body_single_index = i.get_text().strip().replace('\t','').replace('\n','').replace('\xa0','')
            if len(list(body_single_index)) != 0:
                body_temp.append(body_single_index)
        if len(body_temp) == 0:
            return 0, 0
        if len(body_temp[0]) == 17:
            return 0, 0
        
        details_body = body_temp[0][17:]
        details_date = time.strftime('%Y/%m/%d %X')

        return details_date, details_body

    def get_ims_info(self, num):
        url = f'https://ims.tmaxsoft.com/tody/ims/issue/issueView.do?issueId={num}'
        self.driver.get(url)
        time.sleep(1)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # date parsing
        date_list = soup.find_all('span', {'class': 'link2'})

        date_temp = []
        for i in date_list:
            date_single_index = i.get_text().strip().replace('\t','').replace('\n','').replace('\xa0','')
            if len(list(date_single_index)) != 0:
                date_temp.append(date_single_index)

        # check if action exists
        if len(date_temp) == 1:
            return 0, 0
        
        date_index = date_temp[1].find('Registered date') + 18 # registered date index
        ims_date = date_temp[1][date_index:date_index+19]

        # comment parsing
        comment_list = soup.find_all('div', {'class': 'commDescTR data'})

        comment_temp = []
        for i in comment_list:
            comment_single_index = i.get_text().strip().replace('\t','').replace('\n','').replace('\xa0','')
            if len(list(comment_single_index)) != 0:
                comment_temp.append(comment_single_index)
        ims_comment = comment_temp[0]

        return ims_date, ims_comment