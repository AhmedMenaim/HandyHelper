from django.contrib import admin
from Users.models import Users
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# class UsersAdmin(UserAdmin):
#     list_display = ('email', 'username', 'first_name' ,'last_name', 'date_joined','last_login','is_admin','is_staff')
#     search_fields = ('email','username',)
#     readonly_fields = ('date_joined', 'last_login')

#     filter_horizontal = ('permissions',)
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#     fieldsets = ()

admin.site.register(Users)