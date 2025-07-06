from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator

from .forms import RegistroForm, LoginForm

User = get_user_model()

def inicio(request):
    return render(request, 'auth/inicio.html')

@login_required
def home(request):
    return render(request, 'auth/dashboard.html', {'usuario': request.user})

def registro(request):
    es_htmx = request.headers.get('Hx-Request')
    form = RegistroForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user)
        if es_htmx:
            return HttpResponse("""
                <script>
                  window.location.href = '/home/';
                  setTimeout(() => showToast("Cuenta creada con éxito 🎉", "success"), 300);
                </script>
            """)
        response = redirect('home')
        response.set_cookie('toast_register', '1', max_age=5)
        return response

    template = 'auth/partials/form_register.html' if es_htmx else 'auth/register.html'
    return render(request, template, {'form': form})

def login_view(request):
    es_htmx = request.headers.get('Hx-Request')
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            user = User.objects.get(email=email)
            auth_user = authenticate(request, username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                if es_htmx:
                    return HttpResponse("""
                        <script>
                          window.location.href = '/home/';
                          setTimeout(() => showToast("Inicio de sesión exitoso 👋", "success"), 300);
                        </script>
                    """)
                response = redirect('home')
                response.set_cookie('toast_login', '1', max_age=5)
                return response
        except User.DoesNotExist:
            pass
        form.add_error(None, 'Correo o contraseña incorrectos.')

    template = 'auth/partials/form_login.html' if es_htmx else 'auth/login.html'
    return render(request, template, {'form': form})

@login_required
def logout_view(request):
    logout(request)
    response = redirect('login')
    response.set_cookie('toast_logout', '1', max_age=5)
    return response

def password_reset(request):
    form = PasswordResetForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save(
            request=request,
            use_https=request.is_secure(),
            email_template_name='auth/password_reset_email.html',
            subject_template_name='auth/password_reset_subject.txt',
        )
        return redirect('password_reset_done')

    return render(request, 'auth/password_reset.html', {'form': form})

def password_reset_done(request):
    return render(request, 'auth/password_reset_done.html')

def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    validlink = user is not None and default_token_generator.check_token(user, token)

    if not validlink:
        return render(request, 'auth/password_reset_confirm.html', {'validlink': False})

    form = SetPasswordForm(user, request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        response = redirect('password_reset_complete')
        response.set_cookie('toast_pwd_reset', '1', max_age=5)
        return response

    return render(request, 'auth/password_reset_confirm.html', {'form': form, 'validlink': True})

def password_reset_complete(request):
    return render(request, 'auth/password_reset_complete.html')

def auth_switcher(request):
    return render(request, 'auth/partials/switcher.html')
