from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Transaction


@admin.register(Transaction)
class TransactionModelAdmin(admin.ModelAdmin):
    list_display = ["id", "appid", "state", ]


admin.site.unregister(Group)
