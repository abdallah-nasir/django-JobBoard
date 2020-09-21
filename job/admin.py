from django.contrib import admin

# Register your models here.
from .models import job,Category


admin.site.register(Category)
admin.site.register(job)