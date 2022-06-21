from Browser import Browser
from time import sleep
import pandas as pd
from collections import defaultdict

class Bot:
    def __init__(self,base_url,chrome_driver_path,clients_csv,buttons,db,docker):
        self.base_url = base_url
        self.chrome_driver_path = chrome_driver_path
        self.clients = pd.read_csv(clients_csv, sep=";")
        self.db = db
        self.buttons = buttons
        self.docker = docker
    
    def open_browser(self):
        self.browser = Browser(self.chrome_driver_path, self.base_url,self.docker)
    
    
    def make_reservation(self):    
        for i, button in enumerate(self.buttons):
            print(f'Doing the reservation: {i}')
            s = self.clients.iloc[0]
            tranform = defaultdict(list)
            data = s.to_dict(tranform)
            success = self.browser.make_reservation(button,data)
            self.db.save_local(success)
        self.browser.close()
        sleep(2)
        self.db.save_db()

