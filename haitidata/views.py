from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import simplejson as json

def siteindex(request, template='site_index.html'):
    from geonode.search.views import search_page
    post = request.POST.copy()
    post.update({'type': 'layer'})
    request.POST = post
    return search_page(request, template=template)

