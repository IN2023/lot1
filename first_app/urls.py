from first_app import views
from django.urls import re_path

urlpatterns = [
    re_path('', views.reg_log, name="reg_log1"),
]
