from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("IIftWVEztc", views.submit, name="submit"),
    path("<str:project>", views.project)
]

