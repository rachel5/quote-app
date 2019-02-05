from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Post

class PostForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['title'].widget.attrs.update({'class': 'form-control'})
    self.fields['text'].widget.attrs.update({'class': 'form-control'})

  class Meta:
    model = Post
    fields = ('title', 'text')
    labels = {
      'title': _('What do you want this to be called?'),
      'text': _('What do you want to say?')
    }


