from django import forms
from django.contrib.auth.models import User
from .models import S_register, L_register
from base.models import Topic, Marks

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationform(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('passwords didn\'t match')
        return cd['password2']
    
class userEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = S_register
        fields = ('school', 'course', 'year', 'registration_number')

class profileEditLForm(forms.ModelForm):
    class Meta:
        model = S_register
        fields = ('school', 'course', 'year')

class AddTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('name', 'description', 'file')

class StudentMarks(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ('student', 'grade', 'percentage')