from django.contrib import admin

from students.models import *


class ReaderAdmin(admin.ModelAdmin):
    #list_display = [field.name for field in PhysicalPerson._meta.fields]
    list_display = ["name", "id", "work_place", "register_date", "in_date"]
    search_fields = ["name", "id"]
    list_filter = ["category"]
    #exclude = ["ADDRESS"]

    class Meta:
        model = PhysicalPerson


admin.site.register(PhysicalPerson, ReaderAdmin)
admin.site.register(ReaderCategory)


