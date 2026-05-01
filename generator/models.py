from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
    
class Dealership(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Asset(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets/')

class Creative(models.Model):
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)
    background_image = models.ImageField(upload_to='backgrounds/')
    output_image = models.ImageField(upload_to='output/', null=True, blank=True)
    crreated_at = models.DateTimeField(auto_now_add=True)

