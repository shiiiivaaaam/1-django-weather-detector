from django.shortcuts import render
import json 
import urllib.request

# Create your views here.

def index(request):
    if request.method=='POST' and request.POST['city']!='':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=adc4c88b70242d7e962a78f7082c0cbc').read()
        json_data = json.loads(res)
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordination':str(json_data['coord']['lon'])+'                    '+
            str(json_data['coord']['lat']),
            'temp':str(json_data['main']['temp'])+'k',
            'pressure':str(json_data['main']['pressure']),
            'humidity':str(json_data['main']['humidity'])
        }

    else:
        city = ''  
        data ={}  
    return render(request,'index.html',{
        "city":city,'data':data
    })