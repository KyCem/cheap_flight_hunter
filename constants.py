arrival_variant = [
                   {"city" :"prag" ,"city_code" : "prga"},     {"city" :"amsterdam" ,"city_code" : "amsa"},
                   {"city" :"paris" ,"city_code" :  "para"},   {"city" :"milano" ,"city_code" : "mila"}, 
                   {"city" :"barselona","city_code" :  "bcna"},{"city" :"berlin" ,"city_code" : "bera"}, 
                   {"city" :"floransa" ,"city_code" : "flra"}, {"city" :"roma" ,"city_code" : "roma"},  
                   {"city" :"venedik" ,"city_code" : "vcea"},  {"city" :"lyon" ,"city_code" : "lysa"},  
                   {"city" :"kopenhag" ,"city_code" : "cpha"}, {"city" :"bruksel" ,"city_code" : "brua"}, 
                   {"city" :"frankfurt" ,"city_code" : "fraa"},{"city" :"munih" ,"city_code" : "muca"}, 
                   {"city" :"madrid" ,"city_code" : "mada"},   {"city" :"viyana" ,"city_code" : "viea"}, 
                  ]
oneway_departure_date_variants = [
                                  "02.09.2023","03.09.2023","04.09.2023","05.09.2023","06.09.2023","07.09.2023",
                                  "08.09.2023","09.09.2023","10.09.2023","11.09.2023","12.09.2023","13.09.2023",
                                  "14.09.2023","15.09.2023","16.09.2023","17.09.2023","18.09.2023","19.09.2023",
                                 ]
oneway_arrival_date_variants = [
                                "23.09.2023","24.09.2023","25.09.2023",
                               ]
oneway_departure_date_variants_semester = [
                                            "14.01.2024","15.01.2024","16.01.2024","17.01.2024","18.01.2024","19.01.2024",
                                            "20.01.2024","21.01.2024","22.01.2024","23.01.2024","24.01.2024","25.01.2024"
                                          ]


def generateFlightInfo(to_location_city, to_location,oneway_departure_date):
    flight_info ={
        "from_location_city1" : 'istanbul',
        "from_location_city" : 'sofia-havalimani',
              "to_location_city" : to_location_city,
              "from_location1" :  'ista',
              "from_location" :  'sof',
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

