from django.forms import modelform_factory
from django.shortcuts import render, redirect

from Folder.models import VCTroom,personaldata
# Create your views here.
def fold(request,id):
    fold_class = personaldata.objects.get(pk=id)
    return render(request,"website/website.html",{"huawei":fold_class})
def home(request):
    return render(request,'website/home.html',{"jay":VCTroom.objects.all()})


VCTmeeting = modelform_factory(VCTroom,exclude=[])

def newpage(request):
    form = VCTmeeting()
    return render(request,'website/new.html',{"form":form})

def newpage(request):
    if request.method=="POST":
        form=VCTmeeting(request.POST)
        if form.is_valid():
            form.save
            return redirect("jay")
    else:
        form = VCTmeeting()
    return render(request,'website/new.html',{"form":form})
