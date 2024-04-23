from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from productos.models import Producto, CategoriaProducto

def index(request):
    categorias = CategoriaProducto.objects.all()
    productos = Producto.objects.filter(publico=True)
    cattmp = Producto.objects.filter(categoria=1)
    return render(request, 'mainapp/index.html', {
        'titulo': 'Home',
        'categorias': categorias,
        'productos': productos,
        'cattmp': cattmp
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the home page after successful login
            return redirect('index')  # Assuming 'index' is the name of your home page URL
        else:
            # Return an error message or render the login page again with an error message
            return render(request, 'registration/login.html', {'error_message': 'Invalid credentials'})
    else:
        # If it's a GET request, render the login page
        return render(request, 'registration/login.html')
