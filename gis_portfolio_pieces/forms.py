from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, max_length=254, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name', 'style':'width:100%; max-width: 500px; box-sizing: border-box;'}))
    contact_email = forms.CharField(required=True, max_length=254, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Email', 'style':'width:100%; max-width: 500px; box-sizing: border-box;'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Your Message', 'style':'width:100%; max-width: 500px; box-sizing: border-box;'}))
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = ''
        self.fields['contact_email'].label = ''
        self.fields['content'].label = ''
