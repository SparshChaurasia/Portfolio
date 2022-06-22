from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from datetime import datetime


def index(request):
    return render(request, "index.html")

def submit(request):
    if request.method != "POST":
        return HttpResponse("Invalid request method")

    name = request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    message = request.POST.get("message")

    print(name, email, subject, message)

    if not email and message:
        return redirect("/#contact")

    form = Contact(
        Name=name,
        Email=email,
        Subject=subject,
        Message=message,
        Date=datetime.now(),
    )
    form.save()

    return redirect("/#contact")
    
