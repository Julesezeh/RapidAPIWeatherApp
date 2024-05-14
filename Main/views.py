import requests
from django.shortcuts import render

def index(request):
    return render(request,"index.html")


def get_weather(request):
    if request.method == "POST":
        print("get weather running....")

        city = request.POST.get("city")
        scale = request.POST.get("inlineRadioOptions")


        print("scale",scale)
        if scale == "Farenheit":
            query_scale="f"
        elif scale == "Centigrade":
            query_scale="c"

        headers = {
            "X-RapidAPI-Key":"5d90bb0682msh06130921b314cd9p12bc9ajsn5bd773d11d72",
            "X-RapidAPI-Host":"yahoo-weather5.p.rapidapi.com"
        }
        url = "https://yahoo-weather5.p.rapidapi.com/weather"

        params = {"location":city,"format":"json","u":query_scale}

        response = requests.get(url=url,headers=headers,params=params)
        
        jsonResponse = response.json()
        
        location = jsonResponse['location']['city']
        temperature = jsonResponse['current_observation']['condition']['temperature']
        weather_status = jsonResponse['current_observation']['condition']['text']

        print(jsonResponse['current_observation']['condition']['temperature'])
        print("query_scale",query_scale)

        return render(request,'partials/weather_report.html',{"city":location,"temperature":temperature,"status":weather_status, "scale":query_scale})