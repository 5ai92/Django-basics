from django.shortcuts import render

# Create your views here.


def staff_admin(request):
    return render(request, "shared/_main.html")
