from django import forms
from .models import UserRequest

class UserRequestForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = ['request_message']

# forms.py
# forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Remove help text for username and password confirmation fields
        self.fields['username'].help_text = ''
        self.fields['password2'].help_text = ''

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

