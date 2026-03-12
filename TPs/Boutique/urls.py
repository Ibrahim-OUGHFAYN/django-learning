from django.urls import path
from . import views

urlpatterns=[
    path('clients/',views.list_clients,name='clients'),
    path('products/',views.list_products,name='products'),
    path('commandes/',views.list_commandes,name='commandes')
]