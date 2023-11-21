# requisitions/forms.py

from django import forms
from .models import Requisition

class RequisitionForm(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = ['amount', 'approved']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['approved'].widget.attrs['disabled'] = True
        self.fields['approved'].label = 'Approved by Admin'

    def set_admin_permissions(self):
        # Enable the amount field for the admin
        self.fields['amount'].widget.attrs['disabled'] = False
        self.fields['amount'].label = 'Amount (Admin Only)'

    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get('amount')
        approved = cleaned_data.get('approved')

        if approved and not amount:
            raise forms.ValidationError('Amount must be filled in when the requisition is approved.')

        return cleaned_data
