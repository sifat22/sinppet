from django.urls import path
from . import views

urlpatterns = [
    path('', views.snippet_list),
    path('i<int:id>/', views.snippet_detail),
]