from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Jugadores
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR,"templates")'
    )

def base(request):
    return render(request, "base.html")

@login_required
def index(request):
    return render(request, "index.html")

@login_required
def nosotros(request):
    return render(request, "nosotros.html")

@login_required
def contacto(request):
    return render(request, "contacto.html")

@login_required
def api(request):
    return render(request, "api.html")                  

@login_required
def listar(request):
    futbolistas = Jugadores.objects.all()
    datos = {'jugadores' : futbolistas} 
    return render(request, "crud_jugadores/listar.html",datos)

@login_required
def agregar(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('posicion') and request.POST.get('fecha_deb') and request.POST.get('fecha_ret'):
            user =Jugadores()
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.posicion = request.POST.get('posicion')
            user.fecha_deb = request.POST.get('fecha_deb')
            user.fecha_ret = request.POST.get('fecha_ret')
            user.save()
            return redirect('listar')
    else:
        return render(request, "crud_jugadores/agregar.html")

    
@login_required
def actualizar(request):
    if request.method=='POST':
        if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('posicion') and request.POST.get('fecha_deb') and request.POST.get('fecha_ret'):
            user =Jugadores()
            user.id = request.POST.get('id')
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.posicion = request.POST.get('posicion')
            user.fecha_deb = request.POST.get('fecha_deb')
            user.fecha_ret = request.POST.get('fecha_ret')
            user.save()
            return redirect('listar')


    else:
        futbolistas = Jugadores.objects.all()
    datos = {'jugadores' : futbolistas }
    return render(request, "crud_jugadores/actualizar.html",datos)

                
@login_required
def eliminar(request):
    if request.method=='POST':
        if request.POST.get('id'):
           id_borrar = request.POST.get('id') 
           tupla = Jugadores.objects.get(id= id_borrar)
           tupla.delete()
           return redirect('listar')


    else:
        futbolistas = Jugadores.objects.all()
        datos = {'jugadores' : futbolistas }
        return render(request, "crud_jugadores/eliminar.html",datos)

def registro(request):

    if request.method == 'GET':
        return render(request, 'registro.html', {
        'form' : UserCreationForm
    })


    else:
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
                return HttpResponse('Usuario creado con exito.')
            except:
                return render(request, 'registro.html', {
        'form' : UserCreationForm,
        "error": 'Usuario ya existe.'
    })
        return render(request, 'registro.html', {
        'form' : UserCreationForm,
        "error": 'Contraseñas no coinciden.'
    })

def cerrarsesion(request):
        logout(request)
        return redirect ('base')

def iniciar(request):
    if request.method == 'GET' :
        return render(request, "iniciar.html",{
        'form': AuthenticationForm
         })
    else:
        user= authenticate(
            request, username=request.POST['username'], password=request.POST['password']
        )
        if user is None:
            return render(request, 'iniciar.html', 
            {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'


            })
        else:
            login(request, user)
            return redirect('index')
           


            







