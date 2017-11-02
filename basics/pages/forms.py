from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Page


class PageForm(forms.ModelForm):

    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page
        fields = ['title', 'content']
