from django.shortcuts import render

# Create your views here.

def queryAll(request):
    return render(request,'index.html')