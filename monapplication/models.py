from django.db import models
from datetime import date
from random import randint
# Create your models here.
class Filiere(models.Model):
	code = models.CharField(max_length= 3, null= True)
	filiere= models.CharField(max_length= 25, null= True)
	def __str__(self):
		return  self.filiere
		


class Niveau(models.Model):
	code = models.CharField(max_length= 3, null= True)
	niveau= models.CharField(max_length= 25, null= True)
	def __str__(self):
		return     self.niveau
		


class Matiere(models.Model):
	code = models.CharField(max_length= 3, null= True)
	matiere= models.CharField(max_length= 25, null= True)
	coef= models.IntegerField()
	def __str__(self):
		return self.code +" : "+ self.matiere



class Etudiant(models.Model):
	GENRE=[
       ("M", "Masculin"),
       ("F", "Feminin")
	]
	nom= models.CharField(max_length= 25, null= True)
	prenom= models.CharField(max_length= 25, null= True)
	genre= models.CharField(max_length= 15, choices= GENRE, default="M")
	nationalite= models.CharField(max_length= 30, null= True)
	adresse= models.CharField(max_length= 50, null=True)
	telephone= models.CharField(max_length= 17, blank= True)
	date_naiss=models.DateField(auto_now= False)
	photo = models.FileField(upload_to = 'photoEtudiant', blank = True)
	def __str__(self):
		return f" {self.nom} {self.prenom }" 



class Inscription(models.Model):
	matricule= models.IntegerField(null=True, blank=True, unique= True)
	nomPrenom= models.ForeignKey(Etudiant, on_delete= models.CASCADE)
	filiere=models.ForeignKey(Filiere, on_delete= models.CASCADE)
	niveau= models.ForeignKey(Niveau, on_delete=models.CASCADE)
	profil= models.FileField(upload_to="Image_Etudiant")
	annAcademique= models.CharField(max_length= 15, null= True)
	date_inscription= models.DateField(auto_now_add= True)


	def save(self, *args, **kwargs):
		if not self.matricule:
			self.matricule=randint(0, 10000)
			super(Inscription, self).save(*args, **kwargs)
			
	def __str__(self):
		return f"2i-{self.matricule} : {self.nomPrenom}"
    	
			



class Preinscription(models.Model):
	nom_Prenom= models.CharField(max_length= 30, null=True)
	filieres=models.ForeignKey(Filiere, on_delete=models.CASCADE)
	attestation=models.FileField(upload_to="attestation")
	acte_naissance=models.FileField(upload_to="acte_naissance")
	admail= models.EmailField()
	tel= models.CharField(max_length=15, null= True)
	datepreinscription=models.DateField(auto_now_add=True)

	def __str__(self):
		return f'{self.nom_Prenom} - {self.filieres} - {self.datepreinscription}'   




class Contact(models.Model):
	Nom=models.CharField(max_length=30, null=True)
	Prenom=models.CharField(max_length=30, null=True)
	sujet=models.CharField(max_length=60, null=True)
	Email=models.EmailField()
	message=models.TextField()

	def __str__(self):
		return f'{self.Nom} - {self.Prenom} - {self.message}'

class InfoEtudiant(models.Model):
	image = models.FileField(upload_to = "imageInfosEtudiant")
	titre = models.CharField(max_length = 30, null = True)
	text = models.TextField()
	datePub = models.DateTimeField(auto_now_add = True)
	categorie = models.CharField(max_length = 15, choices = [
		("Tous", "Tous"),
		("Licence 1", "Licence 1"),
		("Licence 2", "Licence 3"),
		("Licence 3", "Licence3")
	], default = "Tous")
	def __str__(self):
		return f'{self.titre} - {self.datePub}'


class InfoSession(models.Model):
	image = models.FileField(upload_to = "imageInfosEtudiant")
	titre = models.CharField(max_length = 30, null = True)
	text = models.TextField()
	datePub = models.DateTimeField(auto_now_add = True)
	categorie = models.CharField(max_length = 15, choices = [
		("Tous", "Tous"),
		("Licence 1", "Licence 1"),
		("Licence 2", "Licence 3"),
		("Licence 3", "Licence3")
	], default = "Tous")
	def __str__(self):
		return f'{self.titre} - {self.datePub}'

class InfoBourse(models.Model):
	image = models.FileField(upload_to = "imageInfosEtudiant")
	titre = models.CharField(max_length = 30, null = True)
	text = models.TextField()
	datePub = models.DateTimeField(auto_now_add = True)
	totalEtudiant = models.IntegerField(blank=True, default=1)
	def __str__(self):
		return f'{self.titre} - {self.datePub}'



