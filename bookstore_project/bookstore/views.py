from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Book


class RegisterView(View):
    def get(self, request):
        return render(request, 'bookstore/register.html')

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('book_list')


class LoginView(View):
    def get(self, request):
        return render(request, 'bookstore/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('book_list')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'bookstore/login.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class HomeView(TemplateView):
    template_name = 'home.html'


class BookListView(ListView):
    model = Book
    template_name = 'bookstore/book_list.html'
    context_object_name = 'books'


class AddToCartView(View):
    def get(self, request, book_id):
        cart = request.session.get('cart', [])
        if book_id not in cart:
            cart.append(book_id)
        request.session['cart'] = cart
        return redirect('book_list')


class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', [])
        books = Book.objects.filter(id__in=cart)
        total_price = sum(book.price for book in books)
        return render(request, 'bookstore/cart.html', {'cart_books': books, 'total_price': total_price})

