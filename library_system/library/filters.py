import django_filters
from .models import Books

class BookFilter(django_filters.FilterSet):
    published_date_range = django_filters.DateFromToRangeFilter(field_name='published_date')
    class Meta:
        model = Books
        fields = ['author__name','genre', 'published_date']
