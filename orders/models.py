from datetime import timedelta
from django.db import models

# Create your models here.
from django.utils import timezone
from products.models import Product
from users.models import CustomUser

CHOICES = [
    ('P', 'Processed'),
    ('S', 'Sent'),
    ('D', 'Delivered'),
    ('R', 'Received'),
    ('F', 'Finished')
]


def should_send_date():
    return timezone.now() + timedelta(days=1)


class Order(models.Model):
    ordered_by = models.ForeignKey(CustomUser, related_name='ordered_by', on_delete=models.PROTECT, null=True)
    ordered_product = models.ForeignKey(Product, related_name='ordered_product', on_delete=models.PROTECT, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(default=should_send_date)
    delivery_price = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.CharField(max_length=20, choices=CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
