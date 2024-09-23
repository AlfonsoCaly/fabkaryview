from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}))
    subject = forms.CharField(max_length=100, label='Subject', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message'}), label='Message')
