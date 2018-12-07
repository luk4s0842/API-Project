from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import requests
import datetime

def next_launches(request):
    response = requests.get('https://api.spacexdata.com/v3/launches/upcoming?order=desc')
    data = response.json()

    context = {
        'data':data,
        'title':'Next Launches',
    }
    return render(request, 'spacex_api/show_launches.html', context)

def previous_launches(request):
    response = requests.get('https://api.spacexdata.com/v3/launches/past?order=desc')
    data = response.json()

    context = {
        'data':data,
        'title':'Previous Launches',
    }
    return render(request, 'spacex_api/show_launches.html', context)

def all_launches(request):
    response = requests.get('https://api.spacexdata.com/v3/launches/past?order=desc')
    data = response.json()

    context = {
        'data':data,
        'title':'All Launches',
    }
    return render(request, 'spacex_api/show_launches.html', context)


def details(request, launch_id):
    print("LAUNCH ID: "+str(launch_id))
    response = requests.get('https://api.spacexdata.com/v3/launches/'+str(launch_id))
    data = response.json()

    context = {
        'data':data,
    }
    return render(request, 'spacex_api/details.html', context)
