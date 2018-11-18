from django.db import models

# Create your models here.

class cliente(models.Model):
    nome = models.CharField(max_length=53, blank=False, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField(max_length=3)
    email = models.EmailField()

    def __str__(self):
        return self.nome