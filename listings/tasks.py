from celery import shared_task
from .models import Property
from django.utils import timezone
import datetime
import logging

logger = logging.getLogger(__name__)

@shared_task
def weekly_property_report():
    total_properties = Property.objects.count()
    logger.info(f"{timezone.now()} - Total Properties: {total_properties}")
    return total_properties

