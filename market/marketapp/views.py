from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import  MarketForm

# Create your views here.
from .models import market


def index(request):
    mark=market.objects.all
    return render(request,"home.html",{'result':mark})

def details(request,market_id):
    mark=market.objects.get(id=market_id)
    return render(request,"details.html",{"market":mark})

def add_market(request):
    if request.method=="POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        mark=market(name=name,desc=desc,year=year,img=img)
        mark.save()
    return render(request,"add.html")

def update(request,id):
    mark = market.objects.get(id=id)
    form = MarketForm(request.POST or None, request.FILES ,instance=mark)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form, 'market':mark})
def delete(request,id):
    if request.method=='POST':
        mark=market.objects.get(id=id)
        mark.delete()
        return redirect('/')
    return render(request,'delete.html')



