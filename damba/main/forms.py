from django import forms
from django.core.exceptions import ValidationError

from .models import *

class OrderHouse(forms.Form):
    first_name = forms.CharField(max_length=32, label="Ім'я")
    last_name = forms.CharField(max_length=32, label='Прізвище')
    phone = forms.IntegerField(label='Телефон')
    email = forms.EmailField(label='Email')

    count_of_days = forms.IntegerField(max_value=5, min_value=1, label='Кількість днів')

    house = forms.ModelChoiceField(queryset=Houses.objects.all(), empty_label='Виберіть будинок', label='Будинок')
    # date_booking = forms.DateTimeField()
    date_future_settlment = forms.DateField(label='Дата поселення')
    # date_future_checkout = forms.DateField(label='Дата виселення')
