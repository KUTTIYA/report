
from django.contrib import admin
from django.urls import path, include

from .views import GeneratePDF

urlpatterns = [
    path('generate/pdf/',GeneratePDF.as_view()),
]