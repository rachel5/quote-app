from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Quote

class QuoteForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['attribution'].widget.attrs.update({'class': 'form-control'})
    self.fields['quote_text'].widget.attrs.update({'class': 'form-control'})

  class Meta:
    model = Quote
    fields = ('attribution', 'quote_text', 'quote_source')
    labels = {
      'attribution': _('Attribution'),
      'quote_text': _('Quote'),
      'quote_source': _('Source')
    }


