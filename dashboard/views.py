from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from menu.models import *
# Create your views here.
@login_required
def dashboard(request):
    return render(request,'pages/dashboard.html')

@login_required
def menuitems(request):
    menuitems = MenuItems.objects.all()
    if User.is_authenticated:
        form = menuItemsForm()
        if request.method == 'POST':
            form = menuItemsForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                messages.info(request, "Quotes has been successfully send to Admin, Send Another ")
                return redirect('menuitems')
            else:
                messages.info(request, " Title Should be in English ")
    data = {
        'menuitems': menuitems,
        'form': form,
    }
    return render(request,'pages/menuitems.html',data)

@login_required
def mainmenu(request):
    mainmenu = MainMenu.objects.all()
    form = MenuForm()
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.posted_by = request.user
            instance.save()
            messages.info(request, "Quotes has been successfully send to Admin, Send Another ")
            return redirect('createmainmenu')
        else:
            messages.info(request, " Title Should be in English ")

    data ={
        'mainmenu' : mainmenu,
        'form': form,
    }

    return render(request,'pages/mainmenu.html', data)

@login_required
def updatemenuitems(request,title):
    udata = MenuItems.objects.get(title=title)
    menuitems = MenuItems.objects.all()
    if User.is_authenticated:
        form = menuItemsForm(instance=udata)
        if request.method == 'POST':
            form = menuItemsForm(request.POST, request.FILES, instance=udata)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                messages.info(request, "Quotes has been successfully send to Admin, Send Another ")
                return redirect('menuitems')
            else:
                messages.info(request, " Title Should be in English ")
    data = {
        'menuitems': menuitems,
        'form': form,
    }
    return render(request, 'pages/menuitems.html', data)

def deleteitems(request, title):
    items = MenuItems.objects.get(title=title)
    if request.method == 'POST':
        items.delete()
        return redirect('menuitems')
    data = {
        'items': items,
    }
    return render(request, 'pages/delete.html', data)

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Wrong username and password")
            return redirect('login')
    else:
        return render(request,'pages/login.html')

@login_required
def usermessages(request):
    messages = Contactus.objects.all()
    data ={
        'messages':messages,
    }
    return render(request,'pages/messages.html',data)

def logout(request):
    auth.logout(request)
    return redirect('/')