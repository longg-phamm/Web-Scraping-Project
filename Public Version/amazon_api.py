

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
import time

PATH = ""+os.getcwd()+"/chromedriver"


    
def search (searched_item, driver):
    
    search = driver.find_element_by_id("twotabsearchtextbox")
    search.send_keys(searched_item)
    search.send_keys(Keys.RETURN)
    
    return driver.page_source

def scrap_data(list_of_items):
    
    all_data = []
    for item in list_of_items:
    
        try:
            title = item.h2.text
        except:
            title = "None"
        else:
            title = title.strip()

        
        try:
            url = "https://www.amazon.ca" + item.h2.a.get('href')
        except:
            url = "None"
            
            
        try:
            price = item.find("span", class_= "a-offscreen").text
        except:
            price = "None"
        else:
            price = str(price)
            price.strip(",")
            
        data = {"title": title,"url": url, "price" : price}
        all_data.append(data)
        
    return all_data

def get_items(page_source):
    
    soup = BeautifulSoup(page_source, 'lxml')
    
    items = soup.find_all('div' , {'data-asin': True,'data-component-type': 's-search-result'})
    
    return items
    
    
def store_data(list_of_items):
    
    with open ("amazon-itemsp-database.csv","a") as f:
        fields = ["title", "price", "url"]
        
        writer = csv.DictWriter(f, fieldnames=fields)
        
        for item in list_of_items:
            writer.writerow(item)
            
    return 0;
            


    

    
    
    
    
    
