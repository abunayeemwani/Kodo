from django.shortcuts import render
import requests
import math

# Create your views here.
def index(request):
    sort = ''
    search = ''
    records = "20"
    page = "1"

    url = 'http://127.0.0.1:8000/get_api/?'
    
    if "search" in request.GET:
        url += "search=" + request.GET['search'] +"&"
        search = request.GET['search']
    if "sort" in request.GET:
        url += "sort=" + request.GET['sort'] +"&"
        sort = request.GET['sort']
    if "page" in request.GET:
        url += "page=" + request.GET['page'] +"&"
        page = request.GET['page']
    if "records" in request.GET:
        url += "records=" + request.GET['records'] +"&"
        records = request.GET['records']

    r = requests.get(url)
    json_data = r.json()

    pages = math.ceil(json_data['count']/int(records))

    json_data['sort'] = sort
    json_data['search'] = search
    json_data['records'] = records
    json_data['page'] = page
    json_data['pages'] = range(1,pages+1)
    return render(request, 'assignment1/index.html', json_data)