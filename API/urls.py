
from django.urls import re_path
from API import views


urlpatterns = [
    re_path(r'^department$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),
]
