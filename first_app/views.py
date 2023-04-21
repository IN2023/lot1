from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm, GoodsForm
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt


def funk_1(request):
    return render(request, "first_app/base.html")


@csrf_exempt
def reg_log(request):
    if request.method == "GET":
        form_up = RegisterUserForm
        form_in = LoginUserForm
        return render(request, "first_app/base.html", {"form_in": form_in, "form_up": form_up})
    else:
        form_up = RegisterUserForm(data=request.POST)
        form_in = LoginUserForm(data=request.POST)
        if form_up.is_valid():
            form_up.save()
            return redirect("reg_log1")
        elif form_in.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return render(request, "first_app/home.html")
        return render(request, "first_app/base.html", {"form_in": form_in, "form_up": form_up})


def home(request):
    form_in = GoodsForm
    return render(request, "first_app/home.html", {"form": form_in})
