i = 0
cem = "cem"
import email_sender as email_sender

toplam = "cem" +str(i)
flight_info ={"from_location_city" : 'istanbul'}
kistce = ["cem","kaya","taha", "kocadurmus", "melih", "durhasan"]
oneway_departure_date_variants = ["02.09.2023","03.09.2023","04.09.2023","05.09.2023","06.09.2023","07.09.2023",
                                  "08.09.2023","09.09.2023","10.09.2023","11.09.2023","12.09.2023","13.09.2023",
                                  "14.09.2023","15.09.2023","16.09.2023","17.09.2023","18.09.2023","19.09.2023",
                                  "20.09.2023","21.09.2023","22.09.2023","23.09.2023","24.09.2023","25.09.2023"]
print(kistce[0])
print(len(oneway_departure_date_variants))
for i in range(23):
    print(i)
#email_sender.sendEmail(flight_info['from_location_city'], "aaaaa")
#arrival_variant = [{"city" :"amsterdam" ,"city_code" : "amsa"}, {"city" :"paris" ,"city_code" :  "para"},{"city" :"barselona","city_code" :  "bcna"} ]
#for location_data in arrival_variant:
    #for location_data["value"]
 #   print(location_data['city'] + location_data["city_code"])