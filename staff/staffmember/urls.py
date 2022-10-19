from django.urls import path
from . import views

urlpatterns = [
    path('staffmember/', views.staffinfo),
    path('', views.home, name ="home"),
]
