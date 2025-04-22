from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .models import Book 

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        login(request, user)
        return redirect('book_list') 

    return render(request, 'bookstore/register.html')

from django.contrib import messages
from django.contrib.auth import logout

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('book_list')
#         else:
#             messages.error(request, "Invalid username or password")

#     return render(request, 'bookstore/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return render(request, 'bookstore/login.html')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('book_list')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'bookstore/login.html')


def book_list(request):
    return render(request, 'book_list.html') 

def logout_view(request):
    logout(request)
    return redirect('login')

def add_to_cart(request, book_id):
    cart = request.session.get('cart', [])
    if book_id not in cart:
        cart.append(book_id)
    request.session['cart'] = cart
    return redirect('book_list')

def cart_view(request):
    cart = request.session.get('cart', [])
    books = Book.objects.filter(id__in=cart)
    return render(request, 'bookstore/cart.html', {'cart_books': books})

def home_view(request):
    return render(request, 'home.html')


def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'books': books})
