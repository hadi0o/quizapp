from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'sex', 'age', 'field_of_study', 'city', 'sleep_time')


admin.site.register(Profile, ProfileAdmin)
