from django_filters import rest_framework as filters
from apps.inventory.models import Item

class ItemFilter(filters.FilterSet):
    quantity_min = filters.NumberFilter(field_name='quantity', lookup_expr='gte')
    quantity_max = filters.NumberFilter(field_name='quantity', lookup_expr='lte')
    price_min = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = filters.NumberFilter(field_name='price', lookup_expr='lte')
    
    class Meta:
        model = Item
        fields = ['quantity_min', 'quantity_max', 'price_min', 'price_max',]