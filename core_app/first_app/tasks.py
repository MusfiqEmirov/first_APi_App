from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task


@shared_task
def send_product_creation_email():
    send_mail(
        subject="yatmisiz?",
        message="eger bu mesaji aldizsa  docker isleyir ve product sukunducku yaranir\n"
        "zehmel olmasa bir nezer yetirin\n"
        "https://github.com/MusfiqEmirov/first_APi_App.git ",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=["mammadaliyevmammadali@gmail.com"],
    )

@shared_task
def send_category_creation_email():
    send_mail(
        subject="Category Created ❤️",
        message="Category has been created successfully.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
    )

@shared_task
def send_address_creation_email():
    send_mail(
        subject="Address Created ❤️",
        message="Address has been created successfully.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
    )

@shared_task
def send_supplier_creation_email():
    send_mail(
        subject="Supplier Created ❤️",
        message="Supplier has been created successfully.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
    ) 