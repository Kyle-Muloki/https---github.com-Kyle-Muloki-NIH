# forms.py
from django import forms

class TicketPurchaseForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    ticket_type = forms.ChoiceField(choices=[
        ('3000', 'Early Bird - Kshs 3,000'),
        ('3500', 'Advance - Kshs 3,500'),
        ('4000', 'At Door - Kshs 4,000'),
    ])
    quantity = forms.ChoiceField(choices=[(str(i), str(i)) for i in range(1, 6)])
