from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import requests
import datetime
from .utils import youtube_search
from googleapiclient.errors import HttpError

def show_videos(request, launch_id):
    response = requests.get('https://api.spacexdata.com/v3/launches/'+str(launch_id))
    data = response.json()

    mission_name = data['mission_name']
    try:
        videos = youtube_search(mission_name)
    except HttpError as e:
        print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))

    context = {
        'mission_name':mission_name,
        'videos':videos,
    }
    return render(request, 'spacex_api/show_videos.html', context)


def next_launches(request):
    response = requests.get('https://api.spacexdata.com/v3/launches/upcoming')
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
    response = requests.get('https://api.spacexdata.com/v3/launches?order=desc')
    data = response.json()

    context = {
        'data':data,
        'title':'All Launches',
    }
    return render(request, 'spacex_api/show_launches.html', context)
