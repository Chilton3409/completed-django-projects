from django import forms

class EmailForm(forms.form):
    email = forms.EmailField(label='Email', max_length=128)

    