from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('staffmember/', views.staffinfo),
    path('staff/', views.home, name ="home"),
    path('staffdetail/', views.staffinfo)
]
