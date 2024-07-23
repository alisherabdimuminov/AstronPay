from django.db import models


STATE = (
    ("1", "Hisoblangan"),
    ("2", "To'langan"),
    ("-2", "Bekor qilingan"),
)


class Transaction(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    appid = models.CharField(max_length=100)
    state = models.CharField(max_length=20, choices=STATE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
