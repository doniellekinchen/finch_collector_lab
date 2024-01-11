from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('all-finches/', views.finches_index, name='all-finches'),
    path('all-finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('all-finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('cats/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('cats/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
]