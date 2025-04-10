from django import forms
from contact.models import ContactMessage
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

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
