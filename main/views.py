from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from main.forms import UserCreation, ContactUsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def main(request):
    return render(request, 'main/main.html')


def register(request):
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:main')
    else:
        form = UserCreation()

    context = {'form': form}
    return render(request, 'main/user_creation.html', context)


def place(request):
    return render(request, 'main/place.html')


def activity(request):
    return render(request, 'main/activities.html')


@login_required
def profile(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('main:main')
        else:
            raise ValidationError(f"Current Errors: {form.errors}")

    else:
        form = ContactUsForm()

    context = {'form': form, 'email': request.user.email}
    return render(request, 'main/profile.html', context)
