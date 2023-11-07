from time import sleep 
import pandas as pd
import undetected_chromedriver as uc
import undetected_chromedriver.options as op
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import email_sender as email_sender
import constants

options = Options()
PROXY = "103.49.202.252:80"
options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome()

def find_cheapest_flight(to_location_city, to_location,flightType, oneway_departure_date):
    flight_info = constants.generateFlightInfo(to_location_city, to_location, oneway_departure_date)
    url = constants.giveUrl(flight_info, flightType)
    driver.get(url)
    sleep(11)
    #driver.find_element(By.XPATH, cheapest_button).click()

    #Getting the first x flight ticketresults
    flight_rows = []
    for i in range(2):
        if flightType == "arrival" or flightType == "departure":
            id = 'flight-' + str(i)
            flight_row = driver.find_elements(By.ID, id)
        else:
            class_name = 'matrix_parent_' + str(i)
            flight_row = driver.find_elements(By.CLASS_NAME, class_name)
        flight_rows.append(flight_row)
    sleep(1.6)

    #Insepting the data from flight result rows then getting the data we want
    price_list = []
    for flight_row in flight_rows:
        for WebElement in flight_row:
            elementHTML = WebElement.get_attribute('outerHTML')
            elementSoup = BeautifulSoup(elementHTML, 'html.parser')
        
            #Price
            if flightType == "arrival" or flightType == "departure":
                #temp_price = elementSoup.find("div", {'class' : 'summary-average-price'})
                temp_price = elementSoup.find("span", {'class' : 'money-int'})

            else:
                temp_price = elementSoup.find("div", {'class' : 'flight-summary-price'})
            price_list.append(temp_price.text)
    print(price_list)
    return [price_list, flight_info]


for location_data in constants.arrival_variant:
    date_variants = constants.oneway_departure_date_variants
    print(location_data['city'] + " "+ location_data["city_code"])
    price_list_with_dates = []
    for i in range(len(date_variants)):
        return_list = find_cheapest_flight(location_data['city'],location_data["city_code"],"departure", date_variants[i])
        if return_list is not None and len(return_list[0]) > 0 and float(return_list[0][0]) < 3.000 and return_list[0][0] is not None :
            print(return_list[0][0] + "Uygun Fiyat")
            price_list_with_dates.append("date: " + date_variants[i] +" -> "+ "price: " + str(return_list[0]))
    #Sending the data to email
    subject =  "ISTANBUL" + " -> "  + location_data['city'].upper()
    body = str(price_list_with_dates)
    if len(price_list_with_dates) > 0: 
        email_sender.sendEmail(subject,body) 

def optimizerAlogrithm():
    return 5

def compareWithSofiaFlight():
    return 3
