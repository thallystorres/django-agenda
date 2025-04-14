from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# category (foreign key), show (boolean), picture (imagem)

# Depois
# owner (foreign key)


class Category(models.Model):
    name = models.CharField(max_length=50)  # type: ignore

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)  # type: ignore
    last_name = models.CharField(max_length=50, blank=True)  # type: ignore
    phone = models.CharField(max_length=50)  # type: ignore
    email = models.EmailField(max_length=254, blank=True)  # type: ignore
    created_date = models.DateTimeField(default=timezone.now)  # type: ignore
    description = models.TextField(blank=True)  # type: ignore
    show = models.BooleanField(default=True)  # type: ignore
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,  # type: ignore
    )
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True  # type: ignore
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
