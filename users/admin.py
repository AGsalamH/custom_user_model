from users.Profile import Profile
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import User

# from django.contrib.auth.admin import UserAdmin 
# from .forms import UserRegistrationForm
# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     list_display = ('email',)
#     list_filter = ('groups',)
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ('groups', 'user_permissions',)

#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name')}),
#         (_('Permissions'), {
#             'fields': ('active', 'staff', 'admin', 'groups', 'user_permissions'),
#         }),
#         (_('Important dates'), {'fields': ('last_login',)}),
#     )

#     add_form = UserRegistrationForm
#     form = UserRegistrationForm


admin.site.register(User)
admin.site.register(Profile)