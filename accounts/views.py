from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm



def register(request):
    
    if request.user.is_authenticated:
        if request.user.role == "DONOR":
            return redirect("donor_dashboard")
        elif request.user.role == "NGO":
            return redirect("ngo_dashboard")
        return redirect("home")
    
    if request.method == "POST":
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user=form.save()
            print("USER CREATED:", user.username)
            return redirect("login")
        else:
            print(form.errors)

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def user_login(request):
    if request.user.is_authenticated:
        if request.user.role == "DONOR":
            return redirect("donor_dashboard")
        elif request.user.role == "NGO":
            return redirect("ngo_dashboard")
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            return render(
                request,
                "accounts/login.html",
                {"error": "Invalid username or password"}
            )


    return render(request, "accounts/login.html")

def user_logout(request):

    logout(request)

    return redirect("login")


@login_required
def profile(requst):
    return render(
        requst,
        "accounts/profile.html",
        {
            "user":requst.user
        }
    )