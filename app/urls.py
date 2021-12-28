from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="home"),
    path('contact', views.contact, name='contact-us'),
    path('products', views.products),
    path('product-details/<int:id>', views.product_details),
    path('blog', views.blog),
    path('blog-details', views.blog_details),
    path('testimonials', views.testimonials),
    path('terms', views.terms),
    path('checkout', views.checkout, name="checkout"),
    path('about', views.about),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]