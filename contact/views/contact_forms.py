from django.shortcuts import render, get_object_or_404, redirect
from contact import models
from django.db.models import Q
from django.core.paginator import Paginator


def create(request):
    context = {}
    return render(
        request,
        'contact/create.html',
        context=context
        )
