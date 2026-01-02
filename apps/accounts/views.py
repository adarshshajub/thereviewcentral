from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            if user.is_superuser:
                return redirect("/admin-panel/")
            elif user.is_staff:
                return redirect("/staff/")
            else:
                return redirect("/")
        else:
            return render(request, "auth/login.html", {"error": "Invalid credentials"})

    return render(request, "auth/login.html")
