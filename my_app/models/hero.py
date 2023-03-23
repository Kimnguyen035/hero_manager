from django.db import models
from configs import variable_system as vr_sys

class Hero(models.Model):
    class Meta:
        db_table = vr_sys.DATABASE_TB['HERO_TB']
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    power = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()