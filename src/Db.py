import pandas as pd
class DB:
    def __init__(self,db_path):
        self.db_path = db_path
        self.count =0
        self.db_local = []

    def save_local(self,success):
        print(f'Attemp: {self.count}, success: {success}')
        self.db_local.append({
            'attemp':self.count,
            'success':success
        })
        self.count+=1
    def save_db(self,):
        df = pd.DataFrame(self.db_local)
        df.to_csv(self.db_path)
