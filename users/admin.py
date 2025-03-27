from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "role", "phone", "is_staff", "is_superuser")
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("role", "phone")}),
    )

admin.site.register(User, CustomUserAdmin)

