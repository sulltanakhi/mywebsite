from django.contrib import admin
from .models import Setting
# Register your models here.

class SettigsAdmin(admin.ModelAdmin):
    list_display = ["title"]
admin.site.register(Setting, SettigsAdmin)
