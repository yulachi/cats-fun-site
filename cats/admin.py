from django.contrib import admin

from .models import Visitor


class CatsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Person info", {"fields": ["first_name", "last_name", "gender", "age"]}),
        ("Cat info", {"fields": ["cat_name", "cat_age", "breed"]}),
    ]
    list_display = ("first_name", "last_name", "gender", "age", "cat_name", "cat_age", "breed")
    list_filter = ["age", "gender", "breed"]
    search_fields = ["first_name", "last_name", "cat_name"]


admin.site.register(Visitor, CatsAdmin)
