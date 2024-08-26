from django.forms import ModelForm
from . models import *
from django.forms import fields, widgets 
from django import forms


class PreinscriptionForm(ModelForm):
	class Meta :
		model = Preinscription
		fields = ["nom_Prenom", "filieres", "attestation", "acte_naissance", "admail", "tel"]
		widgets = {
			'nom_Prenom' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'filieres'   : forms.Select(attrs = {'class' : 'form-control'}),
			'attestation': forms.FileInput(attrs = {'class' : 'form-control'}),
			'acte_naissance' : forms.FileInput(attrs = {'class' : 'form-control'}),
			'admail'     : forms.EmailInput(attrs = {'class' : 'form-control'}),
			'tel'         : forms.TextInput(attrs = {'class' : 'form-control'})
		}

		labels = {
			"nom_Prenom" : "Votre nom et prenom",
			"filieres"	 : "Choisissez filiere",
			"attestation": "Attestation de reussite (PDF, PNG)",
			"acte_naissance" : "Acte de naissance (PDF, PNG)",
			"admail"	 : "Adress-Email",
			"tel"		 : "Numero de telephone"
		}

class ContactForm(ModelForm):
	class Meta :
		model = Contact
		fields = ["Nom", "Prenom", "sujet", "Email", "message" ]
	