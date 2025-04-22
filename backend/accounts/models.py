from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class product(models.Model):
    CATEGORY_CHOICES = [
        ("Technology", "Technology"),
        ("Lifestyle", "Lifestyle"),
        ("Travel", "Travel"),
        ("Food", "Food"),
        ("Business", "Business"),
        ("Health", "Health"),
        ("Sports", "Sports"),
        ("Other", "Other"),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="General")
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def edit(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        self.save()


    def short_description(self):
        words = self.description.split()
        if len(words) > 1000:
            return " ".join(words[:1000]) + "..."
        else:
            return self.description


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128) 
    is_active = models.BooleanField(default=True)
    agreed_to_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.username
