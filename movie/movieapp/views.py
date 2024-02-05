from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import mlist
from . forms import editmovie

# Create your views here.

def index(request):
    movie=mlist.objects.all()
    context ={
        "movielist": movie
    }
    # return HttpResponse("hai to movie",context)
    return render(request,"pro1.html",context)

def mshow(request,movie_id):
    movie=mlist.objects.get(id=movie_id)
    context = {
        "movielist": movie
    }
    return render(request,"mpage.html",context)
def addm(request):
    if request.method=='POST':
        name=request.POST.get("aname")
        desc = request.POST.get("desc")
        mdesc = request.POST.get("mdesc")
        img= request.FILES["img"]
        movie=mlist(name=name,desc=desc,mdesc=mdesc,img=img)
        movie.save()
    return render(request,"addmovie.html")
def updatem(request,id):
    movie=mlist.objects.get(id=id)
    form=editmovie(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"updatem.html",{'form':form,'movie':movie })
def deletem(request,id):
    if request.method=='POST':
        movie=mlist.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, "deletem.html")
