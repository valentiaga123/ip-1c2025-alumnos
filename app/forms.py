from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Formulario para el inicio de sesión

class FormularioInicioSesion(AuthenticationForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        # acceder a los campos 'username' y 'password' que ya existen en authenticationform
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre de usuario'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})

# Formulario para el registro de nuevos usuarios


class FormularioCreacionUsuarioPersonalizado(UserCreationForm):
    # Este formulario "hereda" (toma prestado) de UserCreationForm de Django.
    # Eso significa que ya trae automáticamente los campos básicos como:
    # 'nombre de usuario', 'contraseña' y 'contraseña de confirmación'.

    # El método '__init__' es especial; se ejecuta cuando creamos una instancia del formulario.
    # Aca lo usamos para ir campo por campo y añadirles la clase 'form-control' de Bootstrap.
    # Así, todos los campos de este formulario se verán bien con el estilo de tu página.
    def __init__(self, *args, **kwargs):
        # Llama al constructor original de UserCreationForm
        super().__init__(*args, **kwargs)
        # Recorremos cada campo que tiene el formulario
        for nombre_campo, campo in self.fields.items():
            # Y le agregamos a ese campo la clase CSS 'form-control'
            campo.widget.attrs['class'] = 'form-control'


