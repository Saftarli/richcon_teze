from django import forms
from contact.models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email','subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ad Soyad',
                'required': 'required',
                'name': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email ünvanınız',
                'required': 'required',
                'name': 'email',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Mövzu',
                'name': 'subject',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Mesajınız',
                'name': 'message',
            }),
        }