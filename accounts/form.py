from django import forms
from django.db.models.base import Model
from accounts.models import Order
from django.forms import ModelForm, fields
from .models import *


class Orderform(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class Customerform(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
