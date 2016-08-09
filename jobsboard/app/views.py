from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
# Create your views here.

def home(request):
    context= RequestContext(request)
    return render_to_response('index.html', {},context)