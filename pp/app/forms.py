from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

# Form for user signup
# Inherits from UserCreationForm provided by Django
# Adds additional fields like first name, last name, email, and phone number to the signup form
# Overrides the save() method to create a new Customer instance and save it along with the User
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phonenumber = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User  
        fields = ('username', 'first_name', 'last_name', 'email', "phonenumber", 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        customer = Customer(user=user,
                            firstname=self.cleaned_data['first_name'],
                            lastname=self.cleaned_data['last_name'],
                            email=self.cleaned_data['email'],
                            phonenumber=self.cleaned_data['phonenumber']
                            )
        if commit:
            customer.save()
        return user

# Form for updating user profile
# Based on the Customer model
# Allows updating the fields: first name, last name, email, and phone number
# Provides custom widgets for the form fields
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('firstname', 'lastname', 'email' ,'phonenumber')
        widgets={
            'firstname': forms.TextInput(),
            'lastname': forms.TextInput(),
            'email': forms.TextInput(),
            'phonenumber':forms.TextInput(),
        }
    