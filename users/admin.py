from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# admin.site.register(User, UserAdmin)


@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'skin_type')
    filter_horizontal = ('favorite_products',)