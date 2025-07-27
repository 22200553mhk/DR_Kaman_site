# core/admin.py

from django.contrib import admin
from .models import Slider

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'link')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')