from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

class IMSCheckBot:
    def __init__(self, id, pw, ims_nums):
        # driver setting
        self.options = Options()
        self.options.add_argument("headless")
        self.options.add_argument("--window-size=1024,768")
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=self.options)
        self.url = "https://ims.tmaxsoft.com/"
        self.driver.get(self.url)
        self.ims_nums = ims_nums
        time.sleep(3)

        # user info
        self.id = id
        self.pw = pw

    
    def waiting_time(self):
        return random.randint(1, 3) / 10
        

    def log_in(self):
        # login id, pw input field Xpath
        self.id_path = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/input'
        self.pw_path = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/input'
        id_input = self.driver.find_element_by_xpath(self.id_path)
        pw_input = self.driver.find_element_by_xpath(self.pw_path)
        login_button = self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td[3]/input')

        # id input
        id_input.click()
        time.sleep(self.waiting_time())
        id_input.clear()
        time.sleep(self.waiting_time())
        id_input.send_keys(self.id)
        time.sleep(1)
        
        # pw input
        pw_input.click()
        time.sleep(self.waiting_time())
        pw_input.clear()
        time.sleep(self.waiting_time())
        pw_input.send_keys(self.pw)
        time.sleep(0.5)

        login_button.click()

    def find_ims(self):
        ims_num_input_path = '/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[1]/td/a'
        ims_num_input = self.driver.find_element_by_xpath(ims_num_input_path)
        ims_num_input.click()
        time.sleep(self.waiting_time())
        
    def run_program(self):
        try:
            self.log_in()
        except Exception as e:
            print(f"""**Error at login function**
            {e}
            ***************************""")
            exit(0)
        
        try:
            self.find_ims()
        except Exception as e:
            print(f"""**Error at finding IMS**
            {e}
            ***************************""")
            exit(0)