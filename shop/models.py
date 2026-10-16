from django.db import models

ANIMAL_CHOICES = (
    ('cats', 'mushuklar'),
    ('dogs', 'itlar'),
    ('birds', 'qushlar'),
)

CATEGORY_CHOICES = (
    ('foods', 'Ovqatlar'),
    ('toys', "O'yinchoqlar"),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    animal = models.CharField(max_length=20, choices=ANIMAL_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name



class Appointment(models.Model):
    owner_name = models.CharField(max_length=100)
    animal = models.CharField(max_length=20, choices=ANIMAL_CHOICES)
    phone_number = models.CharField(max_length=20)
    pet_name = models.CharField(max_length=100)
    date = models.DateField()
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.owner_name