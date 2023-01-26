from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def main(request):
    return render(request,"plantillas/main.html")


def inicio(request):
    
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('main'))

    else:
        return render(request,"plantillas/main.html")

def historia(request):
    return render(request,'plantillas\historia.html')

def automatizacion (request):
    return render(request,'plantillas/automatizacion.html')

def inteligencia(request):
    return render(request,'plantillas/inteligencia.html')

def nuevas_tec(request):
    if request.user.is_authenticated:
        return render(request, 'plantillas/nuevas_tec.html')
    else:
        return HttpResponse("debes iniciar sesion para acceder")
    

def contac(request):
    if request.user.is_authenticated:
        return render(request,'plantillas/contac.html')
    else:
        return HttpResponse("debes iniciar sesion para acceder")
def salir(request):
    logout(request)
    return redirect('/')


# Create your views here.
