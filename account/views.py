from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        password = request.POST['password']
        print("username", user_name)
        user = auth.authenticate(username=user_name, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "Username is already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return render(request, 'login.html')
        else:
            messages.info(request, "Password and confirm password do not match")
            return redirect('/')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')









