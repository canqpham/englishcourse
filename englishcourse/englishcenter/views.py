#!/usr/bin/python

# -*- coding: utf8 -*-
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Student, Teacher, Course
# Create your views here.


def index(request):
    if request.method == 'POST':
        student_name = request.POST['student_name']
        email = request.POST['email']
        numberphone = request.POST['numberphone']
        address = request.POST['address']
        sex = request.POST['sex']
        datebirth = request.POST['datebirth']

        student_form = Student(name=student_name, number_phone=numberphone,
                           address=address,sex=sex,date_birth=datebirth)
        student_form.save()
    return render(request, 'englishcenter/index.html')
