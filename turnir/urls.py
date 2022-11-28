from django.urls import path

from turnir import views

urlpatterns = [
    path('', views.index, name='index'),
    path('advice/', views.advice, name='advice'),
    path('advice/take/<int:pk>', views.take_advice, name='take_advice'),
    path('docs/', views.docs, name='docs'),
    path('docs/<filename>/', views.docs, name='docs'),
    path('mainkey/', views.mainkey, name='mainkey'),
    path('gener/', views.gener, name='gener'),
]