from django.contrib import admin
from profiles_api import models

class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ['email']



admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.ProfileFeedItem)
