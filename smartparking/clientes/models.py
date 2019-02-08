from django.db import models


class Depart(models.Model):
    nomdepart = models.CharField(max_length = 20)

    def __str__(self):
        return self.nomdepart

class DOC(models.Model):
    tipo = models.CharField(max_length = 20, blank=False, null=False)
    num = models.CharField(max_length = 20, null = False)
    data = models.DateField(auto_now= False)

    def __str__(self):
        return self.tipo + ": " + self.num
    

class Cliente(models.Model):
    nome = models.CharField(max_length=53, blank=False, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    doc = models.OneToOneField(DOC, on_delete = models.CASCADE)
    depart = models.ManyToManyField(Depart)
    def __str__(self):
        return self.nome


class Tel(models.Model):
    numero = models.CharField(max_length = 15)
    descricao = models.CharField(max_length = 50)
    cliente = models.ForeignKey(Cliente,on_delete = models.CASCADE)

    def __str__(self):
        return self.numero
