from django.db import models

# Create your models here.

class Alimento(models.Model):
	nome = models.CharField(max_length=100)
	parte_edibile = models.FloatField() # Parte edibile (g)
	energia_Kcal = models.FloatField() # Energia Kcal	
	energia_KJ = models.FloatField() # Energia KJ	
	acqua = models.FloatField() # Acqua (g)	
	proteine_tot = models.FloatField() # Prot tot (g)	
	proteine_anim = models.FloatField() # Prot anim	
	proteine_veg = models.FloatField() # Prot veg	
	glucidi_tot = models.FloatField()# Glucidi tot	
	amido = models.FloatField() # Amido	
	glucidi_solub = models.FloatField() # Glucidi solub	
	lipidi_tot = models.FloatField() # Lipidi tot	
	saturi = models.FloatField() # Saturi tot	
	monoins = models.FloatField() # Monoins tot	
	polins = models.FloatField()# Polins tot	
	acido_oleico = models.FloatField() # Ac. oleico	
	acido_linoleico = models.FloatField() # Ac. linoleico	
	acido_linolenico = models.FloatField() # Ac. linolenico	
	altri_polins = models.FloatField() # altri Polins	
	colesterolo = models.FloatField() # Colest	
	fibre = models.FloatField() # Fibre alim	
	alcool = models.FloatField() # alcool	
	ferro = models.FloatField() # Ferro	
	calcio = models.FloatField() # Ca
	sodio = models.FloatField() # Na
	potassio = models.FloatField() # K
	fosforo = models.FloatField() # P
	zinco = models.FloatField() # Zn
	vitamina_B1 = models.FloatField() # Vit B1
	vitamina_B2 = models.FloatField() # Vit B2
	vitamina_B3 = models.FloatField() # Vit B3
	vitamina_C = models.FloatField() # Vit C
	vitamina_B6 = models.FloatField() # Vit B6
	acido_folico = models.FloatField() # Folico
	retinolo = models.FloatField() # Retinolo eq
	beta_carotene = models.FloatField() # Beta carotene eq
	vitamina_E = models.FloatField() # Vit E
	vitamina_D = models.FloatField() # Vit D

	def __str__(self):
		return self.nome
