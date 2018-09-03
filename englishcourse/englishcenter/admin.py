# !/usr/bin/python

# -*- coding: utf8 -*-
from django.contrib import admin
from .models import Teacher, Course, Student

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Student)
