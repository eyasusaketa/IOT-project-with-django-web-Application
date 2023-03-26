from django.shortcuts import render
from  django.http import HttpResponse

def log(request):
    return render(render,'login.html')