from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientDashboard/', views.clientDashboard, name= 'clientDashboard'),
    path('jobRequest/', views.jobRequest, name='jobRequest'),
    path('provider/', views.provider, name= 'provider'),
    path('payment/', views.provider, name= 'payment'),
    path('review/', views.review, name= 'review'),
]