from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(blank=True, max_length=20)
    address=models.CharField(blank=True, max_length=200)
    city= models.CharField(blank=True, max_length=200)
    country=models.CharField(blank=True, max_length=200)
    image=models.ImageField(blank=True, upload_to="user_img")

    def __str__(self):
        return f'{self.id}{self.user.username}{self.phone}{self.address}'
       
    def user_name(self):
        return self.user.first_name+' '+self.user.last_name+'['+self.user.username+']'
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="30" />'.format(self.image.url))
    admin_photo.short_description = "Image"
    def imageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

    
    # delete-imagefile-from-path-when-record-is-delete
    # but its working another method which is "pip install django-cleanup"
    # and 'django_cleanup.apps.CleanupConfig', in settings after install
    #  it and its woeking for that i don't use this function which is
    # define below
   
   
    # def remove_on_image_update(self):
    #     try:
    #         # is the object in the database yet?
    #         obj = UserProfile.objects.get(id=self.id)
    #     except UserProfile.DoesNotExist:
    #         # object is not in db, nothing to worry about
    #         return
    #     # is the save due to an update of the actual image file?
    #     if obj.image and self.image and obj.image != self.image:
    #         # delete the old image file from the storage in favor of the new file
    #         obj.image.delete()

    # def delete(self, *args, **kwargs):
    #     # object is being removed from db, remove the file from storage first
    #     self.image.delete()
    #     return super(UserProfile, self).delete(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     # object is possibly being updated, if so, clean up.
    #     self.remove_on_image_update()
    #     return super(UserProfile, self).save(*args, **kwargs)   
        