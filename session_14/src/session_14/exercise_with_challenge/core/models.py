from django.db import models
import logging

logger = logging.getLogger(__name__)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name

    def apply_discount(self, percentage):
        if percentage < 0 or percentage > 100:
            raise ValueError("Discount must be between 0 and 100")
        discount_amount = (self.price * percentage) / 100
        self.price -= discount_amount
        logger.info(f"Applied {percentage}% discount to '{self.name}'. New price: {self.price}")
        self.save()
