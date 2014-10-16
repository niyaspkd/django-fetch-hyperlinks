from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import urllib2
from bs4 import BeautifulSoup
def home(request):
	return render(request,'hello.html')
@csrf_exempt
def he(request):
   k=[]
   name=request.POST.get('name')
   content=urllib2.urlopen(name)
   soup = BeautifulSoup(content)
   links=soup.findAll('a',href=True)
   for link in links:
      k.append(str(link.get("href")))
   return render_to_response('abc.html',{'k':k})
