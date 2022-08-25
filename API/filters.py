from django_filters import rest_framework as filters
from django.forms.widgets import DateInput


from APP.models import Post


class PostFilter(filters.FilterSet):
    date = filters.DateFilter(
        field_name='date',
        widget=DateInput(attrs={'type': 'date'})

    )

    class Meta:
        model = Post
        fields = ['date', 'tags']
