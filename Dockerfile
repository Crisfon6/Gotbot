FROM ubuntu
# update system
RUN apt-get update
RUN apt upgrade -y
# install wget
RUN apt install wget -y
# Install linux essentials
RUN apt install build-essential -y
# install chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \ 
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable
# install python3  and pip
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip


# install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# copy source code
COPY src /src
#allow execute chromedriver
# RUN chmod +x /src/chromedriver
# run application
ENTRYPOINT [ "tail","-f","/dev/null" ]

# ENTRYPOINT [ "python3","/src/main.py" ]

