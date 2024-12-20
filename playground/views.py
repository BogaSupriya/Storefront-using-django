from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html',{'age':'23'})



# Create your views here.
#request -> response
# request handler
# handler