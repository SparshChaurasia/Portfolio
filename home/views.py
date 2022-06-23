from datetime import datetime

from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render

from .models import Contact


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
        messages.error(request, "Missing required fields")
        return redirect("/#contact")

    form = Contact(
        Name=name,
        Email=email,
        Subject=subject,
        Message=message,
        Date=datetime.now(),
    )
    form.save()
    messages.success(request, "Your form was successfully submitted")
    return redirect("/#contact")
    
