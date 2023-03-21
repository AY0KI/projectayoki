from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from app1.models import item,contactMsg
# Create your views here.
def index(request):
     a=item.objects.all()
     print(a)
     return render(request,'ayoki.html',{"det":a})