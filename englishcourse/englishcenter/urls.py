#!/usr/bin/python

# -*- coding: utf8 -*-
from django.urls import path, include
from . import views

app_name = 'englishcourse'

urlpatterns = [
    path('', views.index, name='index')

]