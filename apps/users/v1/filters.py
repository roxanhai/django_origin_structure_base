from django_filters import FilterSet, NumberFilter

from core.filters import FilterSetMixin


class UserFilter(FilterSetMixin, FilterSet):
    id = NumberFilter()
