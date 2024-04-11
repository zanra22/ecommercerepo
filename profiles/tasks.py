# tasks.py
from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import Profile

@shared_task
def check_subscription_expiration():
    today = timezone.now().date()
    expired_subscriptions = Profile.objects.filter(
        is_subscribed=True, subscription_end_date__lte=today
    )
    for profile in expired_subscriptions:
        profile.is_subscribed = False
        profile.save()
        print(profile.is_subscribed)
