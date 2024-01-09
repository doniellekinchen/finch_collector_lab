from django.urls import path

from .import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('all-finches/', views.all_finches, name='all_finches'),
]