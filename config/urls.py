from django.contrib import admin
from django.urls import path

from payment.views import pay

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pay/', pay, name="pay"),
]
