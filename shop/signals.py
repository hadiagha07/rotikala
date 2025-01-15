from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product
from .utils import generate_random_code

@receiver(pre_save, sender=Product)
def generate_product_code(sender, instance, **kwargs):
    if not instance.product_code:
        while True:
            code = generate_random_code()
            if not Product.objects.filter(product_code=code).exists():
                instance.product_code = code
                break