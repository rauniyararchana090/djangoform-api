from django.db import models

# Create your models here.
class Airport(models.Model):
    iata= models.CharField(max_length=100)
    icao= models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    gps= models.CharField(max_length=100)
           
    def __str__(self):    
        return self.iata    

    class Meta:
        db_table="airport"    