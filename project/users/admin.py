from django.contrib import admin
from users.models import MainUser
from django.contrib.auth.admin import UserAdmin


@admin.register(MainUser)
class MainUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email',)
