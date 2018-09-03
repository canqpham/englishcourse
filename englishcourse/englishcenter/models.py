#!/usr/bin/python

# -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models

# -- coding: utf-8
# Create your models here.


class Student(models.Model):

    name = models.CharField(max_length=25)
    number_phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    sex_choices = (('Female', 'Female'),
                  ('Male', 'Male')
                  )
    sex = models.CharField(max_length=6, choices=sex_choices)
    date_birth = models.DateTimeField()

    def __str__(self):
        return self.name


class Teacher(models.Model):

    name_teacher = models.CharField(max_length=25)
    image_teacher = models.ImageField()
    number_phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    subjects = models.CharField(max_length=100)
    identity_card = models.CharField(max_length=20)
    curriculum_vitae = models.FileField(default='Not Found')

    def __str__(self):
        return self.name_teacher


class Course(models.Model):

    name_course = models.CharField(max_length=25)
    image_course = models.ImageField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE , related_name='courses')
    content = models.TextField()

    def __str__(self):
        return self.name_course

    def save(self):
        if not self.image_course:
            return
        image = self.image_course