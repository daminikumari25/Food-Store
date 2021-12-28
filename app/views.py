from django.shortcuts import render, redirect
from app.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View
from django.contrib import messages
from math import ceil
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    Products= PRODUCT.objects.all()
    n= len(Products)
    nSlides= n//3 + ceil((n/3) + (n//3))
    context={'no_of_slides':nSlides, 'range':range(1,nSlides), 'Products': Products}
    return render(request,"index.html", context)

def register_request(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form              
        }
        return render(request, 'register.html', context=context)
    
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form" : form              
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'register.html', context=context)

def login_request(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form' : form
        }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data = request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            context = {
                'form' : form
            }
            return render(request, 'login.html', context=context)
	


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact = CONTACT(name=name, email=email, subject=subject, message=message)
        print(name, email, subject, message)
        Contact.save()
        return redirect("contact-us")
    else:
        return render(request,'contact.html')

def products(request):
    product_list = PRODUCT.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(product_list, 6)
    try:
        Products = paginator.page(page)
    except PageNotAnInteger:
        Products = paginator.page(1)
    except EmptyPage:
        Products = paginator.page(paginator.num_pages)

    return render(request, 'products.html', { 'Products': Products })


def product_details(request, id):
    if request.method == "GET":
        Products = PRODUCT_DETAILS.objects.get(pk=id)
        return render(request,'product-details.html',context={'Products': Products})
    else:
        Products = PRODUCT_DETAILS.objects.get(pk=id)
        Products.quantity = request.POST.get('quantity')
        Products.extra = request.POST.get('extra')
        Products.save()
        return redirect("checkout")

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def terms(request):
    return render(request, 'terms.html')

@login_required(login_url='login')
def checkout(request):
    return render(request, 'checkout.html')

def about(request):
    return render(request, 'about.html')