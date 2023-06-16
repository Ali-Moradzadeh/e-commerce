from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' + f'You have successfully placed an order. Your order ID is {order.id}.'
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    print(32* "*")
    print(mail_sent)
    print(32* "*")
    return mail_sent
