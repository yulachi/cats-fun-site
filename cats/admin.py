from django.contrib import admin

from .models import Person


class CatsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["gender", "age"]}),
        ("Name info", {"fields": ["first_name", "last_name"]}),
    ]
    list_display = ("first_name", "last_name", "gender", "age")
    list_filter = ["age", "gender"]
    search_fields = ["first_name", "last_name"]


admin.site.register(Person, CatsAdmin)
