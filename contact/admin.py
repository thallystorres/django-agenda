from django.contrib import admin
from contact import models
# Register your models here.


@admin.register(models.Contact)
class Contact(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name',
    ordering = '-id',
    search_fields = 'id', 'first_name', 'last_name'
    list_per_page = 20
    list_max_show_all = 100
    list_display_links = 'first_name', 'last_name',
