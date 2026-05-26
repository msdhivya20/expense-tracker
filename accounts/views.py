from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from accounts import views
from django.contrib import messages

def signup_view(request):

    if request.method == "POST":

        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        # EMPTY CHECK
        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect("signup")

        # USER EXISTS CHECK
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        # CREATE USER
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "signup.html")

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        # EMPTY CHECK
        if not username or not password:
            messages.error(request, "Please fill all fields.")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "login.html")
    

def logout_view(request):

    logout(request)

    return redirect('home')

def forgot_username(request):
    if request.method == "POST":
        email = request.POST.get("email")

        user = User.objects.filter(email=email).first()

        if user:
            messages.success(request, f"Your username is: {user.username}")
        else:
            messages.error(request, "Email not found")

    return render(request, "registration/forgot_username.html")