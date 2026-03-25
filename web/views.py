from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import requests
from web.models import Contact, Team, Blog
from django.core.paginator import Paginator

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
    print(context)
    return render(request, "home.html", context)

def about(request):
    teams = Team.objects.all()
    context = {
        "teams":teams
    }
    return render(request, "about.html", context)

def blog(request):
    blog_list = Blog.objects.all().order_by("-create_at")

    paginator = Paginator(blog_list, 6)  # 6 blogs per page
    page_number = request.GET.get("page")
    blogs = paginator.get_page(page_number)

    context = {
        "blogs": blogs
    }

    return render(request, "blog.html", context)


def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)

    prev_blog = Blog.objects.filter(id__lt=blog.id).order_by('-id').first()
    next_blog = Blog.objects.filter(id__gt=blog.id).order_by('id').first()

    context = {
        "blog": blog,
        "prev_blog": prev_blog,
        "next_blog": next_blog
    }

    return render(request, "blog_detail.html", context)
def contact(request):
    if request.method == "POST":
        fullname_ = request.POST.get("fullname")
        email_ = request.POST.get("email")
        subject_ = request.POST.get("subject")
        message_ = request.POST.get("message")

        Contact.objects.create(
            fullname=fullname_,
            email=email_,
            subject=subject_,
            message=message_
        )

        messages.success(request, "Your request submitted successfully.")

        return redirect("contact")   # redirect to avoid resubmission

    return render(request, "contact.html")