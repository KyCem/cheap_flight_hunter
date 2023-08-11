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

options = Options()
PROXY = "103.49.202.252:80"
options.add_argument('--proxy-server=%s' % PROXY)
driver = uc.Chrome()

arrival_variant = [{"city" :"amsterdam" ,"city_code" : "amsa"},{"city" :"paris" ,"city_code" :  "para"},
                   {"city" :"barselona","city_code" :  "bcna"},{"city" :"berlin" ,"city_code" : "bera"}, 
                   {"city" :"prag" ,"city_code" : "prga"},     {"city" :"milano" ,"city_code" : "mila"}, 
                   {"city" :"floransa" ,"city_code" : "flra"}, {"city" :"roma" ,"city_code" : "roma"},  
                   {"city" :"venedik" ,"city_code" : "vcea"},  {"city" :"lyon" ,"city_code" : "lysa"},  
                   {"city" :"kopenhag" ,"city_code" : "cpha"},{"city" :"bruksel" ,"city_code" : "brua"}, 
                   {"city" :"frankfurt" ,"city_code" : "fraa"},{"city" :"munih" ,"city_code" : "muca"}, 
                   {"city" :"madrid" ,"city_code" : "mada"},   {"city" :"viyana" ,"city_code" : "viea"}, 
                 ]
oneway_departure_date_variants = ["02.09.2023","03.09.2023","04.09.2023","05.09.2023","06.09.2023","07.09.2023",
                                  "08.09.2023","09.09.2023","10.09.2023","11.09.2023","12.09.2023","13.09.2023",
                                  "14.09.2023","15.09.2023","16.09.2023","17.09.2023","18.09.2023","19.09.2023",
                                  "20.09.2023","21.09.2023","22.09.2023","23.09.2023","24.09.2023","25.09.2023"]

oneway_departure_date_variants_semester = [
                                  "14.01.2024","15.01.2024","16.01.2024","17.01.2024","18.01.2024","19.01.2024",
                                  "20.01.2024","21.01.2024","22.01.2024","23.01.2024","24.01.2024","25.01.2024"]
def find_cheapest_flight(to_location_city, to_location,oneway, oneway_departure_date):
    flight_info ={"from_location_city" : 'istanbul',
              "to_location_city" : to_location_city,
              "from_location" :  'ista',
              "to_location" : to_location,
              "departure_date" : '02.09.2023',
              "arrival_date" : '14.09.2023',
              "oneway_departure_date" : oneway_departure_date
              }
    if oneway:
        url = "https://www.enuygun.com/ucak-bileti/{flight_info[from_location_city]}-{flight_info[to_location_city]}-{flight_info[from_location]}-{flight_info[to_location]}/?gidis={flight_info[oneway_departure_date]}&yetiskin=1&sinif=ekonomi&save=1&geotrip=international&trip=international".format(flight_info = flight_info)
    else:
        url = "https://www.enuygun.com/ucak-bileti/{flight_info[from_location_city]}-{flight_info[to_location_city]}-{flight_info[from_location]}-{flight_info[to_location]}/?gidis={flight_info[departure_date]}&donus={flight_info[arrival_date]}&yetiskin=1&sinif=ekonomi&save=1&geotrip=international&trip=international".format(flight_info = flight_info)

    driver.get(url)
    sleep(7)
    #driver.find_element(By.XPATH, cheapest_button).click()

    #Getting the first x flight ticketresults
    flight_rows = []
    for i in range(2):
        if oneway:
            id = 'flight-' + str(i)
            flight_row = driver.find_elements(By.ID, id)
        else:
            class_name = 'matrix_parent_' + str(i)
            flight_row = driver.find_elements(By.CLASS_NAME, class_name)
        flight_rows.append(flight_row)
    sleep(1)

    #Insepting the data from flight result rows then getting the data we want
    price_list = []
    for flight_row in flight_rows:
        for WebElement in flight_row:
            elementHTML = WebElement.get_attribute('outerHTML')
            elementSoup = BeautifulSoup(elementHTML, 'html.parser')
        
            #Price
            if oneway:
                #temp_price = elementSoup.find("div", {'class' : 'summary-average-price'})
                temp_price = elementSoup.find("span", {'class' : 'money-int'})

            else:
                temp_price = elementSoup.find("div", {'class' : 'flight-summary-price'})
            price_list.append(temp_price.text)
    print(price_list)
    return [price_list, flight_info]


for location_data in arrival_variant:
    print(location_data['city'] + " "+ location_data["city_code"])
    price_list_with_dates = []
    for i in range(len(oneway_departure_date_variants)):
        date= oneway_departure_date_variants[i]
        return_list = find_cheapest_flight(location_data['city'],location_data["city_code"],True, date)
        if return_list is not None:
            if len(return_list[0]) > 0:
                if float(return_list[0][0]) < 2.500 and return_list[0][0] is not None:
                    print(return_list[0][0] + "Uygun Fiyat")
                    price_list_with_dates.append("date: " + date +" -> "+ "price: " + str(return_list[0]))
        # if   return_list[0] is not None  and float(return_list[0][0]) < 4.100:
            # print(return_list[0][0] + "Uygun Fiyat")
            # price_list_with_dates.append("date: " + date +" -> "+ "price: " + str(return_list[0]))
        # print(return_list[0])
        # price_list_with_dates.append("date: " + date +" -> "+ "price: " + str(return_list[0]))
    #Sending the data to email
    subject = "ISTANBUL -> " + location_data['city'].upper()
    body = str(price_list_with_dates)
    email_sender.sendEmail(subject,body) 



