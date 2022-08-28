from django import forms
from .models import BookQuote

class AddQuotesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(AddQuotesForm, self).__init__(*args, **kwargs)
        self.fields['quotes'].queryset= BookQuote.objects.filter(creator=self.request.user)
    class Meta:
        model = BookQuote
        fields = ['quotes']

    quotes = forms.ModelMultipleChoiceField(
        queryset=None
        )