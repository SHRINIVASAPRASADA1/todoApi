from django.contrib import admin
from . import models

# Register your models here.





@admin.register(models.todo)
class iadmin(admin.ModelAdmin):
    list_display = ("title", "content", "date")

