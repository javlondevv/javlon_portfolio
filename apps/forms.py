from django.db.models import CharField, TextField, EmailField
from django.forms import ModelForm

from apps.models import Contact


class ContactForm(ModelForm):
    name = CharField(max_length=255)
    email = EmailField(max_length=255)
    message = TextField()

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
