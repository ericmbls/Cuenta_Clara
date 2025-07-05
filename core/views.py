from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from .forms import RegistroForm
def registro_view(request):
    form = RegistroForm(request.POST or None)
    es_htmx = request.headers.get('Hx-Request')

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            if es_htmx:
                return HttpResponse('<script>window.location.href="/login/"</script>')
            return redirect('login')
        elif es_htmx:
            return render(request, 'usuarios/partials/form_register.html', {'form': form})

    template = 'usuarios/partials/form_register.html' if es_htmx else 'usuarios/register.html'
    return render(request, template, {'form': form})
def registro_view(request):
    form = RegistroForm(request.POST or None)
    es_htmx = request.headers.get('Hx-Request')

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            if es_htmx:
                return HttpResponse('<script>window.location.href="/"</script>')
            return redirect('login')
        elif es_htmx:
            return render(request, 'usuarios/partials/form_register.html', {'form': form})

    template = 'usuarios/partials/form_register.html' if es_htmx else 'usuarios/register.html'
    return render(request, template, {'form': form})

def verificar_email(request):
    email = request.GET.get('email', '')
    usuario_existe = get_user_model().objects.filter(email=email).exists()

    if usuario_existe:
        return HttpResponse("Ese correo ya está registrado 🤔")
    return HttpResponse('<span class="text-green-600">Correo disponible ✔️</span>')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('bienvenida')

        if request.headers.get('Hx-Request'):
            return render(request, 'usuarios/partials/form_login.html', {
                'error': 'Credenciales inválidas 🫠'
            })
        return render(request, 'usuarios/login.html', {
            'error': 'Credenciales inválidas 🫠'
        })

    template = 'usuarios/partials/form_login.html' if request.headers.get('Hx-Request') else 'usuarios/login.html'
    return render(request, template)

def bienvenida_view(request):
    return render(request, 'usuarios/bienvenida.html')
