from django.shortcuts import render

# Create your views here.

def marque(request):
    return render(request,'marque.html')

def table(request):
    return render(request,'table.html')

def form(request):
    return render(request,'form.html')

def imglink(request):
    return render(request,'imglink.html')

def tagaslink(request):
    return render(request,'tagaslink.html')

def cssselector(request):
    return render(request,'cssselector.html')

def team(request):
    return render(request,'team.html')

def india(request):
    return render(request,'india.html')