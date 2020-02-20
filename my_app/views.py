from django.shortcuts import render
import request
from bs4 import BeautifulSoup

BASE_CRAIGSLIST_URL = "https://sfbay.craigslist.org/search/?query={}"
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    data = request.get()
    print(search)
    context = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', context)