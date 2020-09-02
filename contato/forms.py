from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite o seu nome'}), label='Nome')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Digite o seu e-mail'}), label='E-mail')
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Digite a messagem'}), label='Messagem')
