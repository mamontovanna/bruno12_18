from django.shortcuts import render
from myapp.models import divans
from myapp.models import tables
from django.contrib.auth import authenticate
from django.http import HttpResponse#вывод чего-то
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def test(request):
    if request.method=="POST":
        data=request.POST
        user=authenticate(username=data["log"], password=data["pas"])
        if user:
            request.session['test']="test"
            data=divans.objects.all()
            return render(request, 'divan.html', {"cards":data, "name":str(user)})
        else:
            return HttpResponse("Пользователь не авторизован. Неверное имя пользователя или пароль!")
    return render(request, 'test.html')
def reg(request):
    if request.method=="POST":
        data=request.POST
        new=User.objects.create_user( username = data["log"], password= data["pas"])
        new.save()
        request.session['test']="test"
        data=divans.objects.all()
        n=new.get_username()
        return render(request, 'divan.html', {"cards":data, "name":n})
    else:
        return render(request, 'reg.html')

def start(request):
    return render(request, 'start.html')
def divan(request):
    if request.method=="POST":
        poisk=request.POST
        data=divans.objects.filter(name=poisk["search"]) | divans.objects.filter(color=poisk["search"])
        return render(request, 'divancard.html', {"dat":data})
    else:
        data=divans.objects.all()
        return render(request, 'divan.html', {"cards":data})
def table(request):
    return render(request, 'table.html')
def divanCard(request, post_id):
    if request.method=="GET":
        data=divans.objects.filter(id=post_id)
        return render(request, 'divancard.html',{"dat":data})
    elif request.method=="POST":
        poisk=request.POST
        data=divans.objects.filter(name=poisk["search"]) | divans.objects.filter(color=poisk["search"])
        return render(request, 'divancard.html', {"dat":data})
