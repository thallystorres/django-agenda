from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Registered user')
            return redirect('contact:login')

    context = {
        'form': form
    }

    return render(
        request,
        'contact/register.html',
        context=context,
    )


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Successfully logged in')
            auth.login(request, user)
            return redirect('contact:index')
        messages.error(request, 'Invalid login')
    context = {
        'form': form,
    }

    return render(
        request,
        'contact/login.html',
        context=context,
    )


@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    messages.info(request, 'Logout successful.')
    return redirect('contact:login')


@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {'form': form},
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {'form': form},
        )

    form.save()

    return redirect('contact:user_update')
