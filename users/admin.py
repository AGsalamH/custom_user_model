from users.Profile import Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.utils.translation import gettext_lazy as _


from .models import User
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ('groups',)
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('active', 'staff', 'admin', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)