from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Seu nome...',
            }
        ),
        help_text='Texto de ajuda',
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Seu nome...'
        # })

    class Meta:
        model = Contact
        fields = ("first_name", 'last_name', 'phone',)

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error('first_name', ValidationError('Errooooooo', code='invalid'))

        return super().clean()