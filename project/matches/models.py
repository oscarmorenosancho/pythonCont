from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Match(models.Model):
    name = models.CharField(max_length=255)
    player1 = models.ForeignKey(get_user_model(), null=True,
        on_delete=models.SET_NULL, related_name='player1')
    player2 = models.ForeignKey(get_user_model(), null=True,
        on_delete=models.SET_NULL, related_name='player2')
    score1 = models.DecimalField(max_digits=5, default=0, decimal_places=0)
    score2 = models.DecimalField(max_digits=5, default=0, decimal_places=0)
    startDate = models.DateTimeField( )
