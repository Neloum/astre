from django.db import models

# Create your models here.


class Pole(models.Model):
    lib_pole = models.CharField(max_length=50)

    def __str__(self):
        return self.lib_pole

class Direction(models.Model):
    nom_direc = models.CharField(max_length=50)
    e_mail_secre_direc = models.EmailField(max_length=50)
    secre_direc = models.CharField(max_length=50)
  
    def __str__(self):
        return self.nom_direc

class Site(models.Model):
    lib_site = models.CharField(max_length=50)

    def __str__(self):
        return self.lib_site

class ListeDePersonne(models.Model):
    id_Liste_Pers= models.CharField(max_length=50)
    date_recep = models.DateField(max_length=50)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='listes')

    def __str__(self):
        return f"ListeDePersonne {self.id_Liste_Pers} - {self.direction.nom_direc}- Réception le {self.date_recep}"

class SousDirection(models.Model):
    lib_sous_direc = models.CharField(max_length=50)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='sous_directions')

    def __str__(self):
        return self.lib_sous_direc

class Agent(models.Model):
    nom_ag = models.CharField(max_length=50,null=True, blank=True)
    prenom_ag= models.CharField(max_length=50,null=True, blank=True)
    tel_ag = models.CharField(max_length=15,null=True, blank=True)
    cell_ag = models.CharField(max_length=15,null=True, blank=True)
    sous_direction = models.ForeignKey(SousDirection, on_delete=models.CASCADE, related_name='agents', null=True, blank=True)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='agents', null=True, blank=True)

    def __str__(self):
        return self.nom_ag

class FaireLAstreinte(models.Model):
  
    ListeDePersonne = models.ForeignKey(ListeDePersonne, on_delete=models.CASCADE)
    date_deb = models.DateField()
    date_fin = models.DateField()
    num_sem = models.CharField(max_length=50)
    fichier = models.FileField(upload_to='astreintes/', null=True, blank=True)  # Champ pour stocker le fichier


    def __str__(self):
        return f"Astreinte de la semaine {self.num_sem} - du {self.date_deb} au {self.date_fin} "



class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploaded_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    
