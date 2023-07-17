from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import LandingPage
from crudfornecedor import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@receiver(post_save, sender=LandingPage)
def enviar_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Segue nosso Dashboard AGRO e Dashboard OPERACIONAL'
        recipient_list = [instance.email]
        html_content = render_to_string('email.html', {'nome': instance.nome, 'url_agro': 'https://app.powerbi.com/view?r=eyJrIjoiMmRkYmIzYmMtYmFiZi00ZmRiLThjMjQtM2Y3MmIyNGRkNGNiIiwidCI6Ijk0MmRiNmIyLWVjOWEtNDY4Mi05ZGY1LTM5OWYwMjE3NzFkMCJ9', 'url_pecuaria':'https://app.powerbi.com/view?r=eyJrIjoiOTJhMzQyZmEtNDczOS00NmU1LTlhNDktNTZiOWNkZDAzMDRiIiwidCI6Ijk0MmRiNmIyLWVjOWEtNDY4Mi05ZGY1LTM5OWYwMjE3NzFkMCJ9'})
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, text_content, 'marketing@safegold.com.br', recipient_list)
        msg.attach_alternative(html_content, "text/html")
        msg.send()