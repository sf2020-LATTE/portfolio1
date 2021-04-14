from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Company

admin.site.register(Company)


class CompanyAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags', 'related_companies')

admin.site.register(Company, CompanyAdmin)