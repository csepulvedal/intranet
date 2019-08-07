from django.db import models
 
class Facultad(models.Model):
    fct_id = models.BigIntegerField(primary_key=True)
    fct_nombre = models.CharField(max_length=100, blank=True, null=True)
 
    def __str__(self):
        return self.fct_nombre

class Persona(models.Model):
    prs_rut = models.BigIntegerField(primary_key=True)
    prs_nombre = models.CharField(max_length=100, blank=True, null=True)
    prs_telefono = models.BigIntegerField(blank=True, null=True)
    fct_id = models.ForeignKey(Facultad, models.DO_NOTHING)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.prs_nombre

class Usuario(models.Model):
    usu_usuario = models.CharField(max_length=100, blank=True, null=False)
    usu_password = models.CharField(max_length=100, blank=True, null=False)
    per_id = models.BigIntegerField(blank=True, null=False)
    usu_date = models.DateTimeField('date published')

    def __str__(self):
        return self.usu_usuario