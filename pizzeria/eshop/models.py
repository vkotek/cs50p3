from django.db import models
from django.conf import settings

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_date = models.DateTimeField(null=True)
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, null=True)
    completed_date = models.DateTimeField(null=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=5, null=True)

    def __str__(self):
        return f"{self.id}: {self.order_date} \t {self.total_price}"

class OrderLine(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_id = models.ForeignKey('Order', on_delete=models.PROTECT)
    item = models.ForeignKey('MenuItem', on_delete=models.PROTECT)
    toppings = models.ManyToManyField('ItemTopping')
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=5)
    line_price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.item}\n\tTOPPINGS: {self.toppings}\n\t{self.quantity} x {self.unit_price} = {self.line_price}"

class PaymentMethod(models.Model):
    name = models.CharField(max_length=32, null=True)

    def __str__(self):
        return f"{self.name}"

class MenuItem(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    toppings = models.IntegerField() # How many toppings can you add?

    def __str__(self):
        return f"{self.category} | {self.name} ({self.size.name}) . . . . . . . . ${self.price}"

class ItemTopping(models.Model):
    name = models.CharField(max_length=32)
    allowed_parents = models.ManyToManyField('MenuItem')
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"

class Size(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.id}: {self.name}"
