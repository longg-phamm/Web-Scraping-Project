# Web-Scrapping-Project

Program to scrape product information on the first page of Amazon and Walmart.

## Description

Program scrapes production information (name, price, url) from Amazon or Walmart (user choice) and saves information to a csv file.

### Dependencies

* selenium is needed to run program on web browser. 
* beautifulsoup is needed to scrape product information

### Installing

* install python3 if it has not been installed.
* run `pip install requirements.txt`

### Command-Line Interface

* run `python3 webscrapping.py` followed by OPTIONS  

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
`python3 webscrapping.py -w -u username -p 123456 -n Michael -s noodles`

To discover the options without the need to consulting this page, run `python webscrapping.py --help`
