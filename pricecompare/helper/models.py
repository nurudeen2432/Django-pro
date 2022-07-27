from abc import abstractclassmethod
from django.db import models


class TrackingModel(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        abstractclassmethod=True
        ordering=('-uploaded_at',)