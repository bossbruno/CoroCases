# importing required modules and libraries
import datetime  # to read present date
import time  # to suspend the execution for a specific time
import requests  # to retrieve COVID stats from web
from plyer import notification  # to get notification on the computer

covidStats = None
try:
    covidStats = requests.get('https://corona.lmao.ninja/v2/countries/Ghana?yesterday=null&strict=null&query%20=null')
except:
    # incase the data is not fetched due to lack of internet
    print("Consider checking the internet connection")

if (covidStats != None):
    jsonData = covidStats.json()

    while True:
        notification.notify(
            title="COVID19 Stats on {}".format(datetime.date.today()) + " from " + jsonData['country'],
            message="Total cases : {totalcases}\nToday cases : {todaycases}\nTotal active: {active}\nTotal deaths : {totaldeaths} ".format(

                totalcases=jsonData['cases'],
                todaycases=jsonData['todayCases'],
                totaldeaths=jsonData['deaths'],
                active=jsonData['active'],
                ),
            app_icon="covidProtection.ico",
            timeout=120
        )
        time.sleep(60*60*24)
