from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Clase: formulario de inicio de sesión
class LoginForm(forms.Form):  # Hereda de forms.Form

    # Objeto: campo de email
    # Atributo: configuración del widget para estilo y placeholder
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400',
        'placeholder': 'Correo electrónico'
    }))

    # Objeto: campo de contraseña
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400',
        'placeholder': 'Contraseña'
    }))


# Clase: formulario de registro de usuario
class RegistroForm(forms.ModelForm):  # Hereda de ModelForm para trabajar con el modelo User

    # Objeto: campo personalizado de contraseña
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-2 border rounded',
        'placeholder': 'Contraseña'
    }))

    # Objeto: campo personalizado para confirmar contraseña
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-2 border rounded',
        'placeholder': 'Confirmar contraseña'
    }))

    # Atributo: clase interna Meta para definir configuración del formulario
    class Meta:
        model = User  # Atributo: modelo al que está vinculado el formulario
        fields = ['username', 'email']  # Atributo: campos incluidos del modelo
        widgets = {  # Atributo: configuración visual de los campos
            'username': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded',
                'placeholder': 'Usuario'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-3 py-2 border rounded',
                'placeholder': 'Correo'
            }),
        }

    # Método: validación personalizada para verificar si las contraseñas coinciden
    def clean(self):  # Método sobrescrito
        cleaned_data = super().clean()  # Llama al método original para obtener los datos ya validados

        pwd = cleaned_data.get('password')  # Atributo: valor del campo "password"
        confirm = cleaned_data.get('password_confirm')  # Atributo: valor del campo "password_confirm"

        if pwd and confirm and pwd != confirm:
            # Método: agrega un error al campo "password_confirm" si no coinciden
            self.add_error('password_confirm', 'Las contraseñas no coinciden.')