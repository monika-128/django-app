from django.shortcuts import render
import requests

API_KEY = "e7d8ba293c994bb296094927262402"

def get_ip_info():
    try:
        response = requests.get("https://ipinfo.io/json")
        response.raise_for_status()   # check for request errors
        data = response.json()        # convert response to JSON
        return data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    

def get_current_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        return data
    
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# Create your views here.
def home(request):
    if request.method == "POST":
        city = request.POST.get("city")
        weather_data = get_current_weather(city)

    else:
        city = get_ip_info().get("city")
        weather_data = get_current_weather(city)

        # save session only for IP city
        request.session["temp_c"] = weather_data['current']['temp_c']
        request.session["icon"] = weather_data['current']['condition']['icon']
        request.session["city"] = city

        print(request.session["temp_c"], request.session["city"])

    context = {
        "data": weather_data
    }

    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")
def blog(request):
    return render(request, "blog.html")
def blog_detail(request):
    return render(request, "blog_detail.html")
def contact(request):
    return render(request, "contact.html")