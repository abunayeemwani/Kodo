from django.http import HttpResponse
from django.shortcuts import render
import json
from backend.models import Data

# Search algorithm
def search(data, query):
    print(query)
    res_data = []
    if query == "":
        res_data = data
    else:
        if '"' in query or "'" in query:
            query = query.replace('"', '')
            query = query.replace("'", "")
            res_data = []
            for d in data:
                if query in d['name'] or query in d['description']:
                    res_data.append(d)
        else:
            query_list = query.split()
            res_data = []
            for q in query_list:
                for d in data:
                    if q.lower() in d['name'].lower() or q.lower() in d['description'].lower():
                        if d not in res_data:
                            res_data.append(d)

    return res_data

# Sorting algorithm
def sort(data, sort_key):
    res_data = []
    if sort_key == "name":
        reverse = False
        s_key = "name"
    elif sort_key == "-name":
        reverse = True
        s_key = "name"
    elif sort_key == "date":
        reverse = False
        s_key = "dateLastEdited"
    elif sort_key == "-date":
        reverse = True
        s_key = "dateLastEdited"
    else:
        return data

    res_data = sorted(data, key=lambda i:i[s_key], reverse=reverse)
    
    return res_data


def getAPI(request):
    # read the data.json file
    with open('data.json') as file:
        data = json.load(file)

    # This line of code fetches data from database
    #data = [d for d in Data.objects.all()]

    # default values for records per page and page no
    records_per_page = 20
    page_no = 1

    #getting the value from url using GET method
    if "search" in request.GET:
        data = search(data, request.GET['search'])
    if "sort" in request.GET:
        data = sort(data, request.GET['sort'])
    if "records" in request.GET and request.GET['records'] != "":
        records_per_page = int(request.GET['records'])
    if "page" in request.GET and request.GET['page'] != "":
        page_no = int(request.GET['page'])

    total_posts = len(data)

    # pagination
    show_from = records_per_page * (page_no - 1)
    show_to = records_per_page * page_no
    data = data[show_from:show_to]    
    

    #Final data
    data = {
        "count": total_posts,
        "results": data
    }
    
    return HttpResponse(json.dumps(data))