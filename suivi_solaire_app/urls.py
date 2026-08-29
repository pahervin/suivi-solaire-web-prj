# monitoring/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('get-live-data/', views.get_live_data_json, name='get_live_data'),
]