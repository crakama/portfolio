from django.contrib import admin
from .models import Main

# Register your models here.


class MainAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'reffered_by', 'timestamp', 'updated']

    class Meta:
        model = Main
admin.site.register(Main, MainAdmin)
