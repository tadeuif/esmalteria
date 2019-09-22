from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from .models import Usuario

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        #user.password1 = self.changed_data['password1']
        #user.password2 = self.changed_data['password2']

        if commit:
            user.save()
        
        return user