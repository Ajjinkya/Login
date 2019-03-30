from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    my_dict={'form.as_p':"!!!!!!"}
    return render(request,'registration/login.html',context=my_dict)