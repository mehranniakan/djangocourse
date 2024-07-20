from captcha.fields import CaptchaField
from django import forms

from website.models import Contact, news_letter


class ContactForm(forms.ModelForm):
    Subject = forms.CharField(max_length=255, empty_value=None, required=False)

    class Meta:
        model = Contact
        exclude = ['Created date']
        fields = "__all__"


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = news_letter
        exclude = ['Created date', 'Updated_date', 'Status', ]
        fields = "__all__"
