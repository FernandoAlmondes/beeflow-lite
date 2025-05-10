from django.db import models

# Create your models here.

class Flow(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True, default='Beeflow')
    router = models.GenericIPAddressField(blank=True, null=True, default='192.168.0.10')

    def __str__(self):
        return str(self.router)

    class Meta:
        verbose_name_plural = "Flows"
        unique_together = ('nome', 'router')  # Evita duplicatas