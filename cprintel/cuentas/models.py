from django.db import models

class Agregado(models.Model):
    TIPO_CTA = (
        ('Ahorro', 'Ahorro'),
        ('Corriente','Corriente'),
    )
    nombre_proveedor=models.CharField(max_length=20)
    nombre_banco = models.CharField(max_length=20)
    n_cta = models.CharField(max_length=20,unique=True)
    tipo_cta = models.CharField(max_length=20, choices=TIPO_CTA,null=True)
    observacion = models.TextField(null=True)
    fecha_ag=models.DateField()
    def __str__(self):
        return '%s | %s' %(self.nombre_proveedor,self.nombre_banco)
class Banco(models.Model):
    nombre=models.CharField(max_length=20)
    n_cta=models.CharField(max_length=20,unique=True)
    agregados=models.ManyToManyField(Agregado)
    fecha_b=models.DateField()
    def __str__(self):
        return self.nombre








