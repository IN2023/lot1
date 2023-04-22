from first_app import views
from django.urls import re_path

urlpatterns = [
    re_path(r"^$", views.reg_log, name="reg_log1"),
    re_path(r"^home/$", views.hom, name="home_1"),
    re_path(r"^logout/$", views.log_out, name="logout"),
]
