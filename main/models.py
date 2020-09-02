from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Landlord(models.Model):
    fname = models.CharField(max_length=32, verbose_name='Full name')
    lname = models.CharField(max_length=32, verbose_name='Last name')
    mname = models.CharField(max_length=32, blank=True, null=True, verbose_name='Middle name')
    phone = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=50, unique=True)
    score = models.FloatField(default=0.0, blank=True, null=True, verbose_name='Rank')

    class Meta:
        verbose_name = 'Landlord'
        verbose_name_plural = 'Landlords'

    def __str__(self):
        return self.email


class Contact(models.Model):
    #username = models.CharField(max_length=50, verbose_name='Customer Username')
    email = models.CharField(max_length=50, verbose_name='Customer Email')
    subject = models.CharField(max_length=120)
    message = models.TextField(max_length=1200)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.email) + " - " + str(self.subject)

    class Meta:
        verbose_name = 'Contact Request'
        verbose_name_plural = 'Contact Requests'
        ordering = ['-created']


class ProfileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='media/profile_pics',
                              default='main/avatars/default_avatar.jpg', unique=True)
    created = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        ordering = ['-created']
