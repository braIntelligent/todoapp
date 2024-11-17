from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado con éxito. ¡Ahora puedes iniciar sesión!')
            return redirect('login')
        else:
            messages.error(request, 'Por favor, corrige los errores.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup_app/signup.html', {'form': form})

def custom_404(request, exception):
    return render(request, '404.html', status=404)