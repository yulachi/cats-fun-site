from django.contrib import admin

from .models import AlgoTask


class AlgoAdmin(admin.ModelAdmin):
    list_display = ("a", "h", "r", "m", "timestamp")
    search_fields = ["a", "h", "r", "m"]


admin.site.register(AlgoTask, AlgoAdmin)
