import os
from pathlib import Path
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

    if not all((email, message)):
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


def project(request, project):
    templates = os.listdir(Path(__file__).parent.parent / "./templates/projects/")

    if not any(project == template.split(".")[0] for template in templates):
        messages.error(request, "Invalid project name!")
        return redirect("/")

    return render(request, f"./projects/{project}.html")
