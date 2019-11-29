from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    nome = models.CharField(max_length=60, blank=True, null=True)
    '''seguidores = models.ManyToManyField('Pessoa', blank=True, null=True)

    def get_absolute_url(self):
        return reverse("seguindo", kwargs={"pessoa_id": self.pk})'''

    def __str__(self):
        return self.usuario.username