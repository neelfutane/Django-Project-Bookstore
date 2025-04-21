from django.urls import path
from . import views

urlpatterns = [
     path('books/', views.book_list_view, name='book_list'),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
     path('register/', views.register_view, name='register')
]
