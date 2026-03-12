from django.shortcuts import render
from datetime import date

def list_clients(request):
    clients=[
        {'ncli':'B062','nom':'goffin','localite':'namur','compte':-300},
        {'ncli':'B112','nom':'jack','localite':'poitier','compte':1200},
        {'ncli':'B127','nom':'vanderka','localite':'namur','compte':-4500},
    ]
    return render(request,'Boutique/clients.html',{'clients':clients})

def list_products(request):
    products=[
        {'npre':'CS262','libelle':'chev spain','qstock':200},
        {'npre':'PA45','libelle':'pointe acier','qstock':50},
        {'nre':'PS222','libelle':'pl. spain','qstock':400},
    ]
    return render(request,'Boutique/prodects.html',{'products':products})

def list_commandes(request):
    commandes=[
        {'ncom':302,'ncli':'K111','datecom':date(2008,12,21)},
        {'ncom':242,'ncli':'K231','datecom':date(2008,12,23)},
    ]
    return render(request,'Boutique/commandes.html',{'commandes':commandes})




