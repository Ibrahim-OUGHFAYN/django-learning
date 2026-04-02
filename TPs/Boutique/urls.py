from django.urls import path
from . import views

urlpatterns=[
    path('clients/',views.list_clients,name='clients'),
    path('products/',views.list_produits,name='products'),
    path('commandes/',views.list_commandes,name='commandes'),
    path('details/',views.liste_details,name='details'),
    path('client/<str:id_client>/',views.client_commandes,name="client_commandes")
]