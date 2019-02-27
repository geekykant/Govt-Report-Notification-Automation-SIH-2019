# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

import requests
import json


def showDashboard(request):
    # url = "http://api.openweathermap.org/data/2.5/weather"
    #
    # params = {'lat': request.GET.get('lat', 35), 'lon': request.GET.get('lon', 139),
    #           'appid': 'af9b69f5927b1ad56e894921325ab85e'}
    #
    # location_data = \
    #     {'location_info': params['lat'], 'location_name' : params['lon']
    #      }
    #
    # # weather_api = json.loads(requests.get(url, params).content)
    # #
    # # location_data = \
    # #     {'location_info': weather_api['weather'][0]['main'].encode('utf-8') + " ," + weather_api['weather'][0][
    # #         'description'].encode('utf-8'),
    # #      'location_name': weather_api['name'].encode('utf-8')
    # #      }

    # return render(request, 'website/dashboard/index.html', context=location_data)
    return render(request, 'templates/dashboard/index.html', context='asd')


def about(request):
    return render(request, 'templates/dashboard/about.html')
