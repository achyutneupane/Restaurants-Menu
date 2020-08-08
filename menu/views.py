from django.shortcuts import render,redirect
from.models import Chef,MainMenu,MenuItems
from .forms import *

# Create your views here.

def index(request):
    form = Contactform
    if request.method == 'POST':
        form = Contactform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('home')

    menus = MainMenu.objects.all()
    data = {
        'menus': menus,
        'form':form,

    }
    return render(request,'pages/index.html',data)

def menuitems(request):
    menuitems = MenuItems.objects.all()
    menus = MainMenu.objects.all()

    data = {
        'menuitems':menuitems,
        'menus':menus
    }
    return render(request,'pages/menulist.html',data)

def menudetails(request,name):
    menuitems = MenuItems.objects.filter(main_menu__name=name)
    menus = MainMenu.objects.all()

    data = {
        'title': MainMenu.objects.get(name=name),
        'menuitems' : menuitems,
        'menus': menus,
    }
    return render(request, 'pages/menudetails.html', data)