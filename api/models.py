from django.conf import settings
from django.db import models

class DecksModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, default=1)
    
    name = models.CharField(max_length=65)
    desc = models.TextField(max_length=600)

    
    
    def __str__(self):
        return self.name
    

class Cards(models.Model):
    deck = models.ForeignKey(DecksModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=65)
    desc = models.CharField(max_length=200)
    api_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__()