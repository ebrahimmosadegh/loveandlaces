
from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name and Family *', 'name':'customerName', 'type': 'text', 'id': 'customerName'}),
        validators=[
            validators.MaxLengthValidator(100, 'عنوان پیام شما نمیتواند بیشتر از 200 کاراکتر باشد')
        ]
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Phone *', 'name':'customerPhone', 'type': 'text', 'id': 'customerPhone'}),
        validators=[
            validators.MaxLengthValidator(100, 'عنوان پیام شما نمیتواند بیشتر از 200 کاراکتر باشد')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email *', 'name':'customerEmail', 'type': 'email', 'id': 'customerEmail'}),
        validators=[
            validators.MaxLengthValidator(100, 'ایمیل شما نمیتواند بیشتر از 100 کاراکتر باشد')
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject *', 'name':'contactSubject', 'type': 'text', 'id': 'contactSubject'}),
        validators=[
            validators.MaxLengthValidator(200, 'عنوان پیام شما نمیتواند بیشتر از 200 کاراکتر باشد')
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Message *', 'name':'contactMessage', 'id': 'contactMessage', 'rows': '5',
                   }),
    )


