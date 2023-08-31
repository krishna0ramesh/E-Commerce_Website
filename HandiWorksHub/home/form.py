from django import forms
from .models import orders

class orderform(forms.ModelForm):
    class Meta:
        model = orders
        fields ='__all__'

        labels={
            'recipient':"Name of Recipient",
            'phno':'phone no',
            'item_name':'Item',
            'uid':'unique id',
            'num':'number of items required'

        }