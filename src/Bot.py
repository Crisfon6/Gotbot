from Browser import Browser
from time import sleep
import pandas as pd
from collections import defaultdict

class Bot:
    def __init__(self,base_url,chrome_driver_path,clients_csv,buttons,db):
        self.base_url = base_url
        self.chrome_driver_path = chrome_driver_path
        self.clients =pd.read_csv(clients_csv,sep=";")
        self.db =db
        self.buttons = buttons
    
    def open_browser(self):
        self.browser = Browser(self.chrome_driver_path, self.base_url)
    
    
    def make_reservation(self):    
        for i in self.buttons:
            s = self.clients.iloc[0]
            tranform = defaultdict(list)
            data = s.to_dict(tranform)
            success = self.browser.make_reservation(i,data)
            self.db.save_local(success)
        self.browser.close()
        sleep(2)
        self.db.save_db()

