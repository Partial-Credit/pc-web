from django import forms
from ckeditor.widgets import CKEditorWidget

class ContactForm(forms.Form):
	name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	subject = forms.CharField(required=True)
	message = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'), required=True)