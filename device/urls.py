from django.urls import path, re_path
from .views import Create_Controller, Get_Controller


urlpatterns = [
    re_path(r"^devices/?$", Create_Controller.as_view(), name="create_device"),
    path("devices/<pk>/", Get_Controller.as_view(), name="get_device"),
]
