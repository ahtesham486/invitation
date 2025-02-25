from django import forms
from .models import Invitation

class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['roll_number', 'name', 'whatsapp_phone']
