
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models

BASE_CRAIGSLIST_URL = "https://sfbay.craigslist.org/search/?query={}"
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    response = requests.get("https://sfbay.craigslist.org/search/?query=python%20tutor")
    data = response.text
    print(data)
    context = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', context)