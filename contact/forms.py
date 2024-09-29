from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Enter your name',
            'email': 'Enter your email',
            'message': 'What would you like to know?',
         }
        
        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['name'].widget.attrs["minlength"] = 2
        self.fields['name'].widget.attrs["maxlength"] = 50

        self.fields['email'].widget.attrs['minlength'] = 5
        self.fields['email'].widget.attrs['maxlength'] = 254

        self.fields['message'].widget.attrs['minlength'] = 10
        self.fields['message'].widget.attrs['maxlength'] = 1000
        
        for field in self.fields:
            # Set classes
            self.fields[field].widget.attrs['class'] = 'form form-control mt-3 mb-2'
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            self.fields[field].label = ""
    
    
