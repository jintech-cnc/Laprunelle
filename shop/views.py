from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import user_passes_test
from .models import Category, Product
from .forms import ProductForm, RegisterForm, LoginForm

is_superuser = user_passes_test(lambda u: u.is_superuser)

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-created_at')
    
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'shop/home.html', context)

@is_superuser
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'"{product.name}" a bien été publié dans la boutique.')
            return redirect('manage_products')
    else:
        form = ProductForm()

    return render(request, 'shop/add_product.html', {'form': form, 'editing': False})


@is_superuser
def manage_products(request):
    products = Product.objects.select_related('category').order_by('-created_at')
    return render(request, 'shop/manage_products.html', {'products': products})


@is_superuser
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{product.name}" a bien été mis à jour.')
            return redirect('manage_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/add_product.html', {'form': form, 'editing': True, 'product': product})


@is_superuser
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        name = product.name
        product.delete()
        messages.success(request, f'"{name}" a été retiré de la boutique.')
        return redirect('manage_products')
    return render(request, 'shop/delete_product.html', {'product': product})

def contact(request):
    return render(request, 'shop/contact.html')

def faq(request):
    return render(request, 'shop/faq.html')

def shipping(request):
    return render(request, 'shop/shipping.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Bienvenue chez La prunelle ! Votre compte a été créé.")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'shop/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            form.add_error(None, "Identifiants incorrects.")
    else:
        form = LoginForm()
    return render(request, 'shop/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté(e).")
    return redirect('home')


def about(request):
    return render(request, 'shop/about.html')
