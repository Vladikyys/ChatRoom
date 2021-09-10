from django import forms
from .models import Messages


class MessagesItemForm(forms.Form):
    class Meta:
        model = Messages
        fields = ('author', 'text')
