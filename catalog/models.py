from django.db import models
from django.urls import reverse
from django.forms import ModelForm

# Create your models here.
class RoastProfile(models.Model):

    def __str__(self):
        return f'{self.beans} {self.date}'
    
    #fields
    roast_id = models.UUIDField(primary_key=True)
    date = models.DateTimeField()
    beans = models.TextField(max_length=60)
    weight_in = models.IntegerField()
    weight_out = models.IntegerField()
    batch_num = models.IntegerField()
    batch_of_day = models.IntegerField()
    roasting_notes = models.TextField()
    cupping_notes = models.TextField()
    charge_et = models.FloatField()
    charge_bt = models.FloatField()
    tp_time = models.FloatField()
    tp_et = models.FloatField()
    tp_bt = models.FloatField()
    dry_time = models.FloatField()
    dry_et = models.FloatField()
    dry_bt = models.FloatField()
    drop_time = models.FloatField() # stored as float in seconds
    drop_et = models.FloatField()
    drop_bt = models.FloatField()

    class Meta:
        ordering = ['date']

    # methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

class coffee_stock(models.Model):

    origin_city = models.CharField(max_length=25)
    origin_country = models.CharField(max_length=25)
    varietal = models.CharField(max_length=25)
    process = models.CharField(max_length=25)
    tasting_notes = models.TextField(max_length=200)
    current_stock = models.IntegerField()

    def __str__(self):
        return f'{self.origin_country} {self.origin_city} {self.process} {self.varietal}'
    
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
