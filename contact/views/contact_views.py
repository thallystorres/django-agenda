from django.shortcuts import render, get_object_or_404
from contact import models


def index(request):
    contacts = models.Contact.objects \
        .filter(show=True) \
        .order_by('-id')
    context = {
        'contacts': contacts,
    }
    return render(
        request,
        'contact/index.html',
        context=context
        )


def contact(request, contact_id):
    single_contact = get_object_or_404(
        models.Contact.objects.filter(pk=contact_id, show=True)
        )

    context = {
        'contact': single_contact
    }

    return render(
        request,
        'contact/contact.html',
        context=context
    )
