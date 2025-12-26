from django.db import models

class Sale(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    channel = models.CharField(
        max_length=50,
        help_text="Instagram, Website, WhatsApp, etc."
    )
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} - {self.quantity}"
