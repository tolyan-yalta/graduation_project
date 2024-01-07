from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def order_created(order):
    """Задача для отправки уведомления по электронной почте при успешном создании заказа."""
    email = EmailMessage(subject="Электронная копия чека", # f"Счет # {order.id}"
                        body="Электронная копия чека",
                        to=[order.email],)
    return email
