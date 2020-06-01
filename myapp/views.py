from django.shortcuts import render
from .models import Student
from django.views.generic import ListView
from django.views.generic import DetailView

# Create your views here.

class StudentView(ListView):
    model=Student

class StudentDetail(DetailView):
	model=Student
