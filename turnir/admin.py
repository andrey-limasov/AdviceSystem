from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

from .models import FlagType, Flag, Advice, UserAdvice
from turnir.models import Employee

admin.site.register(Flag)
admin.site.register(FlagType)
admin.site.register(Advice)
admin.site.register(UserAdvice)

flaft = FlagType(description="Флаг за вход в IP камеру")

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)