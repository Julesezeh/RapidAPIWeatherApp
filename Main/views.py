import requests
from django.shortcuts import render

def index(request):
    return render(request,"index.html")


def get_weather(request):
    if request.method == "POST":

        city = request.POST.get("city")
        headers = {
            "X-RapidAPI-Key":"5d90bb0682msh06130921b314cd9p12bc9ajsn5bd773d11d72",
            "X-RapidAPI-Host":"yahoo-weather5.p.rapidapi.com"
        }
        url = "https://yahoo-weather5.p.rapidapi.com/weather"

        params = {"location":city,"format":"json","u":"f"}

        response = requests.get(url=url,headers=headers,params=params)
        
        jsonResponse = response.json()

        print(jsonResponse)

        return render(request,'partials/weather_report.html')