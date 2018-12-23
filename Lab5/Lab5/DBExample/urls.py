from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('models', views.ModelView.as_view()),
    path('addProgram', views.AddProgram.as_view()),
]
