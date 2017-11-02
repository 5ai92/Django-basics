from django.contrib import admin
from .models import Page
from django import forms

from ckeditor.widgets import CKEditorWidget

# Register your models here.


class PageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page
        fields = '__all__'


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm


admin.site.register(Page, PageAdmin)

