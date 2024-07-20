from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def signupview(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("User created successfully.")  # Debugging line
            return redirect('login.html')
        else:
            print("Form is not valid:", form.errors)  # Debugging line
    else:
        form = SignupForm()
    return render(request, "signup.html", {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print("User authenticated and logged in.")  # Debugging line
            return redirect('next')
        else:
            print("Invalid username or password.")  # Debugging line
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, "login.html", {})

@login_required
def next_view(request):
    print("Inside next_view.")  # Debugging line
    return render(request, "next.html", {})