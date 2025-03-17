from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings
from .models import (Product,
                     Category,
                     Adress,
                     Supplier)

from first_app.tasks import (
    send_product_creation_email,
    send_category_creation_email,
    send_address_creation_email,
    send_supplier_creation_email,
)


@receiver(post_save, sender=Product)
def my_product_handler(sender, **kwargs):
    send_product_creation_email.delay()

@receiver(post_save, sender=Category)
def my_category_handler(sender, **kwargs):
    send_category_creation_email.delay()

@receiver(post_save, sender=Adress)
def my_address_handler(sender, **kwargs):
    send_address_creation_email()  

@receiver(post_save, sender=Supplier)
def my_supplier_handler(sender, **kwargs):
    send_supplier_creation_email()
    