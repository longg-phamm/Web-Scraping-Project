# Web-Scrapping-Project

Program to scrape product information on the first page of Amazon and Walmart.

## Description

Program scrapes production information (name, price, url) from Amazon or Walmart (user choice) and saves information to a csv file.

### Dependencies

* selenium is needed to run program on web browser. 
* beautifulsoup is needed to scrape product information

* NOTE: the current version of ChromeDriver works with chrome browser version 97.0 Please check your chrome browser version and download the corresponding chromedriver at https://chromedriver.chromium.org/downloads

### Installing

* install python if it has not been installed.
* run `pip install requirements.txt`

### Command-Line Interface

* run `python webscrapping.py` followed by OPTIONS  

### OPTIONS

Where to search
* `--amazon` or `-a` to select scrapping on Amazon
* `--walmart`or `-w` to select scrapping on Walmart

Walmart credential
* `--username` or `-u` followed by the username
* `--password` or `-p` followed by the password
* `--name` or `-n` followed by the name of the account (or any name you want, this is for clarification purpose for information stored in the csv file

To search
* `--search` or `-s` followed by the item to be searched

Example, searching for noodles on Walmart:
`python webscrapping.py -w -u username -p 123456 -n Michael -s noodles`

To discover the options without having to consult this page, run `python webscrapping.py --help`


## UPDATE January 2022
* Walmart updated their capcha test and bot detection, might take sometime to rewrite the walmart API to by pass their new captcha test. Next plan is to allow the option of scrapping product information off Walmart WITHOUT login
