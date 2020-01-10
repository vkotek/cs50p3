from django.db import models

# Create your models here.
class Item(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    toppings = models.IntegerField() # How many toppings can you add?

    def __str__(self):
        return f"{self.category} | {self.name} ({self.size.name}) . . . . . . . . ${self.price}"

class Topping(models.Model):
    name = models.CharField(max_length=32)
    allowed_parents = models.ManyToManyField('Item')
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.id}: {self.name}"

class Size(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.id}: {self.name}"