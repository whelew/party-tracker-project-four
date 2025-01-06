# home/signals.py

from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from allauth.account.models import EmailAddress

@receiver(user_signed_up)
def user_signed_up_handler(request, user, **kwargs):
    # Check if email is already linked to the user
    if not EmailAddress.objects.filter(user=user).exists():
        email_address = EmailAddress(user=user, email=user.email, primary=True, verified=True)
        email_address.save()
        print(f"Email {email_address.email} linked to user {user.username}")
