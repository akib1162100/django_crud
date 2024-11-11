from venv import logger

from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Books
import  logging
logger = logging.getLogger(__name__)


@receiver(post_save,sender=Books)
def log_book_create(sender,instance,created,**kwargs):
    if created:
        logger.info(f"Book created: {instance.title} by {instance.author}")

@receiver(post_delete,sender=Books)
def log_delete_book(sender,instance,**kwargs):
    logger.info(f"Book deleted: {instance.title} by {instance.author}")