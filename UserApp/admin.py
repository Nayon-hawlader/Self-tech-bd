from django.contrib import admin

# Register your models here.

from UserApp.models import UserProfile



class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('id','user','phone','address','country','admin_photo')
    list_filter=['user']


admin.site.register(UserProfile, UserProfileAdmin)