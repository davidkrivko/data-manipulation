from django.contrib import admin

from .models import UserModel, CategoryModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender', 'birth_date', 'category')
    list_filter = ('category', 'gender', 'birth_date')
    search_fields = ('first_name', 'last_name', 'email')


admin.site.register(UserModel, UserModelAdmin)
admin.site.register(CategoryModel)
