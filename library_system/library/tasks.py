from celery import shared_task
from datetime import datetime,timedelta
from .models import Books

@shared_task
def archive_books():
    cutoff_date = datetime.today() - timedelta(days=365*10)

    Books.objects.filter(published_date__lte=cutoff_date,is_archived=False).update(is_archived=True)