from django.shortcuts import render
from django.http import HttpResponse
def home (request):
    return render(request,'home.html',{'name':"Hari"})
def add(request):
    val=int(request.POST["num1"])
    val2=int(request.POST["num2"])
    res=val+val2
    return render (request,"result.html",{"result":res})

# Create your views here.
