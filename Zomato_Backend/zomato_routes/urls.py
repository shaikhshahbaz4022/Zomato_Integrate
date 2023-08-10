
from django.urls import path
from . import views

urlpatterns = [
    path("create", views.Create, name="Create"),
    path("get", views.GetData, name="getData"),
    path('update', views.UpdateData, name="update"),
    path('delete', views.DeleteData, name="delete"),

]
