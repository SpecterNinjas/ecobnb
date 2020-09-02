from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Contact, ProfileImage


class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreation, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['email'].required = True
        self.fields['username'].help_text = ""
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""

    def save(self, commit=True):
        user = super(UserCreation, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']

        if commit:
            user.save()
        return user

    def clean(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists! Please, enter another email address.")
        return self.cleaned_data


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'subject', 'message']

    def save(self, commit=True):
        user = super(ContactUsForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.subject = self.cleaned_data['subject']
        user.message = self.cleaned_data['message']

        if commit:
            user.save()
        return user

    def clean(self):
        email = self.cleaned_data['email']
        if not (User.objects.filter(email=email).exists() and User.objects.filter(email=email).count() == 1):
            raise ValidationError("Only registered users can post message.")
        if not len(self.cleaned_data['subject']) <= 120:
            raise ValidationError("Subject is too long. Maximum length needs to be 120.")
        if not len(self.cleaned_data['message']) <= 1200:
            raise ValidationError("Message is too long. Maximum length needs to be 1200.")

        return self.cleaned_data



