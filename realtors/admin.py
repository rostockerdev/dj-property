from django.contrib import admin
from django.contrib.admin.decorators import register

from realtors.models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 20

admin.site.register(Realtor, RealtorAdmin)
