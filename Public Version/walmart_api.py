from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import os
import csv
import time


#PATH = ""+os.getcwd()+"/chromedriver"
    
def search (searched_item, driver):
    """
    Function to search for product
    """
    pass_capcha(driver)

    search = driver.find_element_by_id("global-search-input")
    search.send_keys(searched_item)
    time.sleep(5)
    search.send_keys(Keys.RETURN)
    
    pass_capcha(driver)
    
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-title-link.line-clamp.line-clamp-2.truncate-title>span")))

    return driver.page_source

def extract_data(list_of_items):
    """
    Function to extract data from product
    """
    
    all_data = []
    for item in list_of_items:
    
        #title
        try:
            a = item.find("a",class_="product-title-link line-clamp line-clamp-2 truncate-title")
            title = a.span.text
        except:
            title = "None"
        else:
            title = title.strip()

        #url
        try:
            div = item.find("div",style = "height: 200px;")
            url = "https://www.walmart.com" + div.a.get('href')
        except:
            url = "None"
        else:
            url = url.replace(" ","%20")
            
        #price
        price_range = []
        price_range_tag = item.find("span", class_="product-variant-price")
        if (price_range_tag != None):
            prices = price_range_tag.find_all("span",{"class" : "price price-main"})
                       
            if (len(prices) != 0):
                for price in prices:
                    price = price.find("span", class_="visuallyhidden")
                    price_range.append( price.text.strip(","))
                    
        else:
            try:
                span = item.find("span", class_="price-main-block")
                price_range.append( span.find("span", class_="visuallyhidden").text)
                       
            except:
                price_range.append("None")
                   
        #append data
        if len(price_range) != 2:
            data = {"title": title,"url": url, "1st price" : price_range[0], "2nd price": "None", "Price range display" : "FALSE"}
        else:
            data = {"title": title,"url": url, "1st price" : price_range[0], "2nd price": price_range[1], "Price range display" : "TRUE"}
        all_data.append(data)
        
    return all_data

def scrape_items(page_source):
    """
    Function to scrape products from the site
    """
    soup = BeautifulSoup(page_source, 'lxml')
    
    items = soup.find_all('div' , {'data-id': True, 'class' : 'search-result-gridview-item-wrapper'})
    
    return items
    
    
def store_data(list_of_items, username):
    """
    Function to store data
    """
    try:
        os.mkdir("./Data")
    except OSError as e:
        print("Directory exists")
          
    with open ("./Data/"+"walmart-items-database.csv","a") as f:
        fields = ["title", "1st price", "2nd price" ,"Price range display", "url"]
        
        writing = csv.writer(f)
        writing.writerow([username])
        writer = csv.DictWriter(f, fieldnames=fields)
        
        for item in list_of_items:
            writer.writerow(item)
            
    return 0
            
def login (user,password,driver):
    """
    Function to login into walmart
    """

    Account = driver.find_element_by_id("hf-account-flyout")
    Account.click()
    
    Signin = driver.find_element_by_link_text("Sign In")
    Signin.click()
    
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_all_elements_located( (By.ID, "remember-me")))
    
    time.sleep(2)
    
    email = driver.find_element_by_id("email")
    email.send_keys(user)
    
    time.sleep(5)
    
    credential = driver.find_element_by_id("password")
    credential.send_keys(password)
    time.sleep(5)
    credential.send_keys(Keys.RETURN)
    
    pass_capcha(driver)
                
    try:
        wait.until(EC.visibility_of_all_elements_located( (By.ID, "global-search-input")))
    except:
        print("Login Unsuccesful")
        return 1
           
    print("Login Success")
    return 0
    
    
def pass_capcha (driver):
    """
    Function to by-pass the captcha test
    """
        
    status = 0
    
    try:
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_all_elements_located( (By.ID, "px-captcha")))
    except:
        print("No Capcha Found")
        status = 1
        
    if (status == 0):
    
        print("Capcha Found")
        try:
        
            captcha = driver.find_element_by_id("px-captcha")
            action = ActionChains(driver)
            
            action.move_to_element(captcha)
            action.click_and_hold(captcha)
            action.pause(10)
            action.release()
            
            action.perform()
            
            time.sleep(8)
            
        except:
            print("Capcha fail")
    
    
    
    
    
    
