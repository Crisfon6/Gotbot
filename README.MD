# Testing Front GotDibs

This program use selenium for do testing from a **Google Chrome** the input are the data for fill the form, the ouput is a **CSV** the route of this file is in ```./src/data/db.csv``` with the next fields:

| Field | Mean |
|-------|------|
|attemp |# attempt|
|success| **true :** if the attempt was successfully **false:** failed|  

docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:latest
## Requirements :
Install GoogleChome : https://www.google.com/intl/es/chrome/?brand=YTUH&gclid=CjwKCAjwqauVBhBGEiwAXOepkfUnBVw4AppW-XZuRIT7FHBEPbyAr_0LXqwrL10zT9Fi0_CMgwLg5RoCe9IQAvD_BwE&gclsrc=aw.ds


For use this bot you need download the Chrome driver :
https://chromedriver.chromium.org/,
give execution permission and add this file in the folder ```./src/driver/```


Set the data for fill the form in the csv. path: ```./src/data/clients.csv```


## Execution:
```
    #install dependencies 
    pip3 install -r requirements.txt
    #move to the folder with execution file
    cd src
    # execute 
    python3 main.py
```

## Issues

### Mac 
Unlisted webdriver from list programs malicious 
```
xattr -d com.apple.quarantine chromedriver 

```