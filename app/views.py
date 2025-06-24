# capa de vista/presentación

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .layers.services import services
from django.contrib.auth.models import User

# AGREGO desde app/forms.py
from .forms import FormularioInicioSesion, FormularioCreacionUsuarioPersonalizado


def spinner(request):
    return render(request, 'spinner.html')

# EXISTENTE
def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados: uno de las imágenes de la API y otro de favoritos, ambos en formato Card, y los dibuja en el template 'home.html'.


def home(request):
    # Llama a la función que implementaste en service.py
    images = services.getAllImages()
    return render(request, 'home.html', {'images': images})

# función utilizada en el buscador.

def search(request):
    name = request.POST.get('query', '')

    # si el usuario ingresó algo en el buscador, se deben filtrar las imágenes por dicho ingreso.
    if (name != ''):
        # Llama a la nueva función de filtrado por nombre
        images = services.filterByCharacter(name)

        return render(request, 'home.html', {'images': images})
    else:
        return redirect('home')

# función utilizada para filtrar por el tipo del Pokemon


def filter_by_type(request):
    type = request.POST.get('type', '')
    if type != '':
        # Llama a la nueva función de filtrado por tipo
        images = services.filterByType(type)
        return render(request, 'home.html', {'images': images})
    else:
        return redirect('home')

# NUEVA VISTA DE AUTENTICACION


def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        formulario = FormularioInicioSesion(request, data=request.POST)

        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            return redirect('home')
    else:
        formulario = FormularioInicioSesion()

    return render(request, 'registration/login.html', {'formulario': formulario})


# REGISTRAR NUEVOS USUARIOS
# guarda el usuario
def registrar_usuario(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        formulario = FormularioCreacionUsuarioPersonalizado(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect('home')
    else:
        formulario = FormularioCreacionUsuarioPersonalizado()

    return render(request, 'registration/register.html', {'formulario': formulario})

# Estas funciones se usan cuando el usuario está logueado en la aplicación.


@login_required  # ajustamos esta vista
def cerrar_sesion(request):
    logout(request)
    return redirect('login')
