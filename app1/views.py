from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request,'ayoki.html')