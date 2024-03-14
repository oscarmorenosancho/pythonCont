"""
    Models of docu
"""

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Token(models.Model):
    id = models.CharField(max_length=300, primary_key=True, unique=True)
    owner = models.ForeignKey(get_user_model(), null=True,
        on_delete=models.CASCADE, related_name='owner')
    used = models.BooleanField(default=False)
    class Meta:
        indexes = [ models.Index("owner", "used", name="owner_used") ]

