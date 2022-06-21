from Bot import Bot
import os
import sys
import math
from Db import DB

def main():
    base_url = 'https://static.got-dibs.com/dealership-demo/cars.html' #put your url
    buttons = [
            '/html/body/section[3]/div/div/div[2]/div/div[1]/div/div[3]/button',
            '/html/body/section[3]/div/div/div[2]/div/div[2]/div/div[3]/img',
            '/html/body/section[3]/div/div/div[2]/div/div[3]/div/div[3]/button',
            '/html/body/section[3]/div/div/div[2]/div/div[4]/div/div[3]/img',
            '/html/body/section[3]/div/div/div[2]/div/div[5]/div/div[3]/button',
            '/html/body/section[3]/div/div/div[2]/div/div[6]/div/div[3]/img'
        ]  
    max_buttons = len(buttons)
    os.system('clear')
    print('='*18)
    print('Hi i am GotBot 🤖')
    print('='*18)
    n_attemps = int(input('Numbers of reservations or 0 for exit: '))
    #docker = input('Use docker?(y/n)')
    docker = 'n'
    if (docker in ['y','Y']):
        docker = True
    else:
        docker = False
    if (n_attemps<=0):
        print('Good bye 👋🏻')
        return
    db = DB(f'{sys.path[0]}/data/db.csv')
    mod_attemp =  n_attemps%max_buttons
      # all buttons for do reservations
    max_bots= n_attemps/max_buttons
    for i in range(math.ceil(max_bots)):
        buttons_for_bot =buttons
        if(math.ceil(max_bots)==i+1 & mod_attemp>0):            
            buttons_for_bot =buttons[:mod_attemp] 
        bot = Bot(base_url,f'{sys.path[0]}/driver/chromedriver',f'{sys.path[0]}/data/clients.csv',buttons_for_bot,db,docker)
        bot.open_browser()
        bot.make_reservation()

if __name__ == '__main__':
    main()
