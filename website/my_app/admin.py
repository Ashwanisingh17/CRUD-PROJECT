from django.contrib import admin
from my_app.models import Student


# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','description']
