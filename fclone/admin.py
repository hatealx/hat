from django.contrib import admin
from .models import LoginRecord

@admin.register(LoginRecord)
class LoginRecordAdmin(admin.ModelAdmin):
    list_display = ('contact', 'created_at')
