import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
import stripe
from .models import City, Comment
from .forms import CityForm, BlogPostForm, RegisterForm
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

pub_key = 'pk_test_cV5Fqg1yaTYLigI26KmLVa63'
stripe.api_key = "sk_test_5HQYAAH2KPVEFyIbogrduxfC"


def index(request):
    comment = Comment.objects.order_by('-date')
    context = {'pub_key': pub_key, 'comment': comment}
    return render(request, 'forex/index.html', context)


def about(request):
    return render(request, 'forex/about.html')


def full_width(request):
    return render(request, 'forex/full-width.html')


def services(request):
    return render(request, 'forex/services.html')


def pricing(request):
    return render(request, 'forex/pricing.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print('Invalid registartion')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'forex/contact.html', context)


def payment_stripe(request):
    pass


def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=217e3198b0fb547325eddd84ee9e3b5b'

    weather_data = []
    #this is for getting the form when it's submitted
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],

        }
        weather_data.append(city_weather)
    context = {'r': weather_data, 'form': form}
    return render(request, 'forex/weather.html',  context)


def BlogPost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            # take the data
            form.save()
            return redirect('index')
    else:
        form = BlogPostForm()

    context = {'form': form}
    return render(request, 'forex/Blogpost.html', context)


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response
     

        

    
        
        



