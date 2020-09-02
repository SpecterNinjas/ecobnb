from django.contrib import admin
from .models import Landlord, Contact, ProfileImage

admin.site.register(Landlord)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject', 'created']


class ProfileImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'created']
    list_filter = ['created']


admin.site.register(Contact, ContactUsAdmin)
admin.site.register(ProfileImage, ProfileImageAdmin)
