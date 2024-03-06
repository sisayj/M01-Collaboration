from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('webapp/', views.home, name='webapp_home'),
]