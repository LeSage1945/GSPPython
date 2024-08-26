
from django.urls import path
from . import views

urlpatterns = [
    path("",views.accueil, name="accueil"),
    path("contactpage",views.contact, name="contact"),

    path("preinscription", views.preinscription, name="preinscription"),
    path("resul", views.resultat, name="resultat"),
    path("etud", views.etudiant, name="etudiant"),
    path("bour", views.bourse, name="bourse"),
    path("infEtud", views.etudiantInfos, name="etudiantInfos"),
    path("sess", views.session, name="session"),
    path("detail/<int:id>/", views.detailEtu, name="detailEtudiant")

]
