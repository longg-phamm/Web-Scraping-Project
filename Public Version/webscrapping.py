

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import argparse
import csv
import time
import walmart_api as wmt
import amazon_api as amz
import os

PATH = ""+os.getcwd()+"/chromedriver"

def run_browser(url):

    driver = webdriver.Chrome(PATH)
    driver.get(url)

    return driver


if __name__ == '__main__':
    
    argparser = argparse.ArgumentParser(description="Scrape Amazon or Walmart")
    group = argparser.add_mutually_exclusive_group()
    group.add_argument("--amazon", "-a", action = "store_true", help="If specified, the program will scrape Amazon")
    group.add_argument("--walmart", "-w", action = "store_true",help="If specified, the program will scrape Walmart")

    
    argparser.add_argument("--username", "-u", help="The username to login if on Walmart")
    argparser.add_argument("--password", "-p", help="The password to login if on Walmart")
    argparser.add_argument("--name", "-n", help="Name of the account")
    
    argparser.add_argument("--search", "-s",help="keywords to search")
   
    args = argparser.parse_args()

    #walmart branch. If user wants to scrape walmart, they neeeds account credential
    if args.walmart is True:
    
        if args.username == None or args.password == None or args.name == None:
            print("Unable to login without account credentials")
            
        if args.search == None:
            print("Unable to search without keywords")
            
        else:
            driver = run_browser("https://www.walmart.com")
                
            wmt.pass_capcha(driver)
            time.sleep(5)

            login_status = wmt.login(args.username,args.password,driver)
            
            if ( login_status[0] == 0 ):
                html = wmt.search(args.search, driver)
                
                items = wmt.get_items(html)

                alldata = wmt.scrap_data(items)

                result = wmt.store_data(alldata, args.name)

                if (result == 0):
                    print("Data retrieved succesfully")
                else:
                    print("Data retrieved unsuccesfully")
                
                driver.quit()
            
    #Amazon branch. If user wants to scrape amazon, they do not need account credential
    if args.amazon is True:
        driver = run_browser("https://www.amazon.com")
        
        time.sleep(5)
        
        html = amz.search(args.search, driver)

        items = amz.get_items(html)

        alldata = amz.scrap_data(items)

        result = amz.store_data(alldata)

        if (result == 0):
            print("Data retrieved succesfully")
        else:
            print("Data retrieved unsuccesfully")
           
    
        
    
    
    

    
    
    
    
    
