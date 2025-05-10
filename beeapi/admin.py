from django.contrib import admin

# Register your models here.
from .models import Flow

class FlowAdmin(admin.ModelAdmin):
    list_display = ['id','router']
admin.site.register(Flow, FlowAdmin)