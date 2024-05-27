from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EmpleadoForm(ModelForm):

    class Meta:
        model = Empleado
        fields = '__all__'

class SubirProyectoForm(ModelForm):

    class Meta:
        model = SubirProyecto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']