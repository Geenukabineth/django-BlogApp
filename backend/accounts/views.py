from django.shortcuts import render, redirect, get_object_or_404
from .models import product
from django.http import HttpResponse, HttpResponseRedirect
from .forms import productForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def product_list(request):
    Products = product.objects.all()
    return render(request, "index.html", {"products": Products})


def product_detail(request, pk):
    product = get_object_or_404(product, pk=pk)
    return render(request, "base.html", {"product": product})


@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect(request, "registration/signup.html")

        try:
            user = User.objects.create_user(username=username, email=email, password=password)  
            messages.success(request, "Account created successfully!")
            return redirect("login")

        except Exception as e:

            messages.error(request, f"An error occurred during signup: {str(e)}")
            return redirect("login")
    else:
        return render(request, "registration/signup.html")




def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser or user.is_staff:
                return HttpResponseRedirect(reverse("base"))  
            else:
                return render(request, "index.html", {"data": user})
        else:
            return render(request, "registration/login.html", {"error": "Invalid username or password"})
    else:
        return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    return redirect("index")


@login_required
def base(request):
    dbitem=product.objects.all()
    context =  {"dbitem": dbitem}
    
    return render(request, "base.html", context)


def create_product(request):
    if request.method == "POST":
        form = productForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully!")
            return redirect("base")  
    else:
        form = productForm()

    return render(request, "page/create.html", {"form": form})


@login_required 
def update(request, id):
    Product = product.objects.get(pk=id)

    Product.name = request.POST.get("name")
    Product.save()
    return redirect("base")


@login_required
def delete(request, id):
    Product = product.objects.get(pk=id)
    Product.delete()
    
    return redirect("base")
