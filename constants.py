arrival_variant = [
                   {"city" :"prag" ,"city_code" : "prga"},     {"city" :"amsterdam" ,"city_code" : "amsa"},
                   {"city" :"paris" ,"city_code" :  "para"},   {"city" :"milano" ,"city_code" : "mila"}, 
                   {"city" :"barselona","city_code" :  "bcna"},{"city" :"berlin" ,"city_code" : "bera"}, 
                   {"city" :"floransa" ,"city_code" : "flra"}, {"city" :"roma" ,"city_code" : "roma"},  
                   {"city" :"venedik" ,"city_code" : "vcea"},  
                   {"city" :"kopenhag" ,"city_code" : "cpha"}, {"city" :"bruksel" ,"city_code" : "brua"}, 
                   {"city" :"frankfurt" ,"city_code" : "fraa"},{"city" :"munih" ,"city_code" : "muca"}, 
                    
                  ]
oneway_departure_date_variants = [
                                  "08.12.2023","15.12.2023",
                                 ]
oneway_arrival_date_variants = [
                                "23.09.2023","24.09.2023","25.09.2023",
                               ]


def generateFlightInfo(to_location_city, to_location,oneway_departure_date):
    flight_info ={
        "from_location_city" : 'istanbul',
        "from_location_city1" : 'sofia-havalimani',
              "to_location_city" : to_location_city,
              "from_location" :  'ista',
              "from_location1" :  'sof',
              "to_location" : to_location,
              "departure_date" : '02.09.2023',
              "arrival_date" : '14.09.2023',
              "oneway_departure_date" : oneway_departure_date
              }
    return flight_info

def giveUrl(flight_info,urlType):
    departureUrl = "https://www.enuygun.com/ucak-bileti/{flight_info[from_location_city1]}-{flight_info[to_location_city]}-{flight_info[from_location1]}-{flight_info[to_location]}/?gidis={flight_info[oneway_departure_date]}&yetiskin=1&sinif=ekonomi&save=1&geotrip=international&trip=international".format(flight_info = flight_info)
    arrivalUrl = "https://www.enuygun.com/ucak-bileti/{flight_info[to_location_city]}-{flight_info[from_location_city1]}-{flight_info[to_location]}-{flight_info[from_location1]}/?gidis={flight_info[oneway_departure_date]}&yetiskin=1&sinif=ekonomi&save=1&geotrip=international&trip=international".format(flight_info = flight_info)
    twoWayUrl = "https://www.enuygun.com/ucak-bileti/{flight_info[from_location_city]}-{flight_info[to_location_city]}-{flight_info[from_location]}-{flight_info[to_location]}/?gidis={flight_info[departure_date]}&donus={flight_info[arrival_date]}&yetiskin=1&sinif=ekonomi&save=1&geotrip=international&trip=international".format(flight_info = flight_info)
    if urlType == "arrival":
        return arrivalUrl
    elif urlType == "departure":
        return departureUrl
    elif urlType == "twoWay":
        return twoWayUrl

