from django.db import models

# Create your models here.

class Maker(models.Model):
    name =  models.CharField(max_length=100)

    def __init__(self):
        return f'{self.name}'
    
    def to_json(self):
        return {
            "id" : self.id,
            "name" : self.name
        }

class Product(models.Model):
    name =  models.CharField(max_length=100)
    description = models.TextField()
    image1_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)
    image4_url = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    maker = models.ForeignKey(
        Maker,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    category = models.ForeignKey("Category", on_delete=models.SET(" "), null=False)


    def __str__(self) -> str:
        return f"{self.name} : {self.description}"
    
    def to_json(self):
        return {
            "id": self.pk,
            "name": self.name,
            "produced_in": self.produced_in,
            "image-1": self.image1_url,
            "image-2": self.image2_url,
            "image-3": self.image3_url,
            "image-4": self.image4_url,
            "price" : self.price
        }
    

class Category(models.Model):
    name = models.CharField(max_length=200)

    parent_category = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name="children_categories",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            "id": self.pk,
            "name": self.name,
        }

