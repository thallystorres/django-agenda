from django.db import models
from django.utils import timezone
# Create your models here.

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)  # type: ignore
    last_name = models.CharField(max_length=50, blank=True)  # type: ignore
    phone = models.CharField(max_length=50)  # type: ignore
    email = models.EmailField(max_length=254, blank=True)  # type: ignore
    created_date = models.DateTimeField(default=timezone.now)  # type: ignore
    description = models.TextField(blank=True)  # type: ignore

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
