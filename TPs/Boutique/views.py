from django.shortcuts import render,get_object_or_404
from .models import Client,Produit,Commande,Detail

def list_clients(request):
    data_clients=Client.objects.all()
    return render(request,'Boutique/clients.html',{'clients':data_clients})

def list_produits(request):
    data_produits=Produit.objects.all()
    return render(request,'Boutique/prodects.html',{'produits':data_produits})

def list_commandes(request):
    data_commandes=Commande.objects.select_related('client').all()
    return render(request,'Boutique/commandes.html',{'commandes':data_commandes})


def liste_details(request):
    data_details=Detail.objects.select_related('commande','produit').all()
    return render(request,'Boutique/details.html',{'details':data_details})

def client_commandes(request,id_client):
    client=get_object_or_404(Client,ncli=id_client)

    commandes=Commande.objects.filter(client=client).prefetch_related('lignes__produit')

    return render(request,'Boutique/client_commandes.html',{
        'client':client,
        'commandes':commandes
    })
