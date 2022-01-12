

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import csv
import time

#PATH = os.getcwd()+"/chromedriver"


    
def search (searched_item, driver):

    """
    Function to search products
    """
    search = driver.find_element_by_id("twotabsearchtextbox")
    search.send_keys(searched_item)
    search.send_keys(Keys.RETURN)
    
    return driver.page_source

def extract_data(list_of_items):
    """
    Function to extract data from product
    """
    
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

def scrape_items(page_source):
    """
    Function to scrape product (product tags) from the site
    """
    
    soup = BeautifulSoup(page_source, 'lxml')
    
    items = soup.find_all('div' , {'data-asin': True,'data-component-type': 's-search-result'})
    
    return items
    


def store_data(list_of_items):
    """
    Function to store data to folder Data. It will create folder Data if has not created
    """
    try:
       os.mkdir("./Data")
    except OSError as e:
       print("Directory exists")
       
    with open ("./Data/" + "amazon-itemsp-database.csv","a") as f:  #https://stackoverflow.com/questions/54944524/how-to-write-csv-file-into-specific-folder
        fields = ["title", "price", "url"]
        
        writer = csv.DictWriter(f, fieldnames=fields)
        
        for item in list_of_items:
            writer.writerow(item)
            
    return 0;
            


    

    
    
    
    
    
