from django.db import models
from django.conf import settings

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_date = models.DateTimeField(null=True)
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, null=True)
    completed_date = models.DateTimeField(null=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=5, null=True)

    def __str__(self):
        return f"{self.id}: {self.order_date} \t {self.total_price}"

class PaymentMethod(models.Model):
    name = models.CharField(max_length=32, null=True)

    def __str__(self):
        return f"{self.name}"

class Detail(models.Model):
    order_id = models.ForeignKey('Order', on_delete=models.PROTECT)
    item = models.ForeignKey('menu.Item', on_delete=models.PROTECT)
    toppings = models.ManyToManyField('menu.Topping')
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=5)
    line_price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.item}\n\tTOPPINGS: {self.toppings}\n\t{self.quantity} x {self.unit_price} = {self.line_price}"