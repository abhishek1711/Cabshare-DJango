from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import UserProfile
from accounts.models import Post

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',

            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',

        )

class TravForm(forms.ModelForm):
    # From = forms.CharField(widget=forms.TextInput(
    # attrs={
    #     'class':'form-control',
    #     'placeholder':'write a post....'
    # }
    #
    # ))
    class Meta:
        model = Post
        fields = ('route','date','time','phone_no')
