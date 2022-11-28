from django.contrib import admin

# Register your models here.

from .models import FlagType, Flag, Advice, UserAdvice

admin.site.register(Flag)
admin.site.register(FlagType)
admin.site.register(Advice)
admin.site.register(UserAdvice)

flaft = FlagType(description="Флаг за вход в IP камеру")