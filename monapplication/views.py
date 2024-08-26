from django.shortcuts import render, redirect
from . models import * 
from . formulaire import *
from . models import*
from django.contrib import messages

# Create your views here.
def accueil(request):
	return render(request, "index.html")

def contact(request):
	cont = Contact.objects.all()
	if request.method == "POST":
		form = ContactForm(request.POST).save()
		return redirect("contact")

	form = ContactForm()

	return render(request, "contact.html")

def niveau(request):
	return render(request, "niveau.html")	


def resultat(request):
	return render(request, "resultat.html")

	

def etudiant(request):
	listeEtudiant = Inscription.objects.all().order_by('-id')[:3]
	context = {
	"liste" : listeEtudiant,
	"totalEtudiant": listeEtudiant.count()
	}
	return render(request, "etudiant.html", context)

def bourse(request):
	#chargement des information bourse 
	les_bourse = InfoBourse.objects.all()
	context = {
	"mesBourses" : les_bourse
	}
	return render(request, "bourse.html", context)

def session(request):
	
	lesSessions = InfoSession.objects.all().order_by("-id")
	context = {
	"mesSessions": lesSessions
	}
	return render(request, "session.html", context)

def etudiantInfos(request):
	lesInfos = InfoEtudiant.objects.all().order_by("-id")
	totalInfos = lesInfos.count()
	context = {
	"mesInfos": lesInfos,
	"totalInfos": totalInfos
	}
	return render(request, "etudiantInfos.html", context)

def detailEtu(request, id):
	etudiantDetail = Inscription.objects.get(id = id)
	context = {
	"mesDetails": etudiantDetail
	}
	return render(request, "detailetudiant.html", context)

def preinscription(request):
	preins = Inscription.objects.all()
	filieres = Filiere.objects.all()

	if request.method == "POST":
		forms = PreinscriptionForm(request.POST, request.FILES).save()
		messages.success(request, (f"merci {request.POST['nom_Prenom']} votre preinscription a ete faite avec succes !"))
		return redirect("preinscription")
	forms = PreinscriptionForm()

	context = {
		"filiere" : filieres,
		"form"   : forms
	}
	return render(request, "preinscription.html", context)

