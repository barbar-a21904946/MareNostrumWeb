from django.db import models

#create your models here

class Tarefa(models.Model):
    titulo= models.CharField(max_length=30)
    prioridade=models.IntegerField(default=1)
    concluida=models.BooleanField(default=False)
    criado=models.DateTimeField(auto_now_add=True)