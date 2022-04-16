from django.contrib import admin
from django.forms import Textarea

from .models import *
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'first_name', 'user_name', 'phone')
    list_filter = ('email', 'first_name', 'user_name', 'is_active', 'is_staff', 'phone')
    ordering = ('-id',)
    list_display = ('email', 'first_name', 'is_active', 'is_staff', 'phone')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2',
                       'is_active', 'is_staff', 'phone')}
         ),
    )


admin.site.register(User, UserAdminConfig)

