from argparse import Action
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
from time import sleep

class Browser:
    def __init__(self,driver_path,base_url):
        self.driver_path = driver_path
        self.base_url = base_url
        self.setup_browser()
        

    def setup_browser(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        # self.driver = webdriver.Safari()
        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        try:
            self.driver.get(self.base_url)
        except Exception as e:
            print('Error getting Chrome driver: ' + str(e))

    def make_reservation(self,button_xpath,data):        
        try:            
            #wait until reserform-name
            WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,button_xpath))).click()
            name_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "reserveform-name")))
            name_input.send_keys(data['name'])
            sleep(1)
            email_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "reserveform-email")))
            email_input.send_keys(data['email'])
            sleep(1)
            phone_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "reserveform-phone")))
            phone_input.send_keys(data['phone'])
            phone_input.send_keys(Keys.TAB)
            sleep(1)
            for i in str(data['card_number']):
                ActionChains(self.driver)\
                    .send_keys(i).perform()
            for i in str(data['card_date']):
                ActionChains(self.driver)\
                    .send_keys(i).perform()
            for i in str(data['card_cvc']):
                ActionChains(self.driver)\
                    .send_keys(i).perform()
            for i in str(data['zip_code']):
                ActionChains(self.driver)\
                    .send_keys(i).perform()
                
            sleep(2)
            ActionChains(self.driver)\
                .send_keys(Keys.TAB).perform() 
            ActionChains(self.driver)\
                .send_keys(Keys.ENTER).perform() 
            ActionChains(self.driver)\
                .send_keys(Keys.ENTER).perform() 
                      
            try:
                WebDriverWait(self.driver,35).until(EC.text_to_be_present_in_element(
            (By.ID,
             "gotdibs-reservation-message"), "Your vehicle has been reserved, the dealer will contact you shortly"))          
                success=True
            except Exception as e:
                print(e)
                success =False            
            #close modal
            self.driver.find_element_by_id('gotdibs-modal-close').click()
            return success
        except Exception as e:
            print('Error getting reservation: ' , str(e))
            self.driver.close()
    def close(self):
        self.driver.close()
