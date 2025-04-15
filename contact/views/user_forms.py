from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Registered user')
            form.save()
            redirect('contact:index')

    context = {
        'form': form
    }

    return render(
        request,
        'contact/register.html',
        context=context,
    )
