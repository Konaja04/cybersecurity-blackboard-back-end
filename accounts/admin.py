from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contra', 'creado')
    search_fields = ('nombre', 'contra')
