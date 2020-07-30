from django.forms import ModelForm
from .models import Item
from .models import Stock


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
