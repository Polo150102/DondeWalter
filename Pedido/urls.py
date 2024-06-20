from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('carta/', views.carta, name='carta'),
    path('detalle_plato/<str:tipo_comida>/<int:id>/', views.detalle_plato, name='detalle_plato')
]
