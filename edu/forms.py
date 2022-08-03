from django import forms
from django.core.validators import MinLengthValidator, RegexValidator
from . import models


class UserRegisterForm(forms.Form):
    firstname = forms.CharField(max_length=30, validators=[MinLengthValidator(limit_value=1)])
    lastname = forms.CharField(max_length=30, validators=[MinLengthValidator(limit_value=1)])
    username = forms.CharField(max_length=30, validators=[MinLengthValidator(limit_value=5)])
    password1 = forms.CharField(
        label="Password",
        max_length=40,
        validators=[MinLengthValidator(limit_value=8), RegexValidator(r'^[A-Za-z0-9]+$')],
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label="Confirm password",
        max_length=40,
        validators=[MinLengthValidator(limit_value=8), RegexValidator(r'^[A-Za-z0-9]+$')],
        widget=forms.PasswordInput()
    )
    email = forms.EmailField()


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput())


class FeedbackForm(forms.Form):
    title = forms.CharField(max_length=50, validators=[MinLengthValidator(limit_value=1)])
    text = forms.CharField(max_length=250, validators=[MinLengthValidator(limit_value=10)], widget=forms.Textarea())
    email = forms.EmailField()


class UserProfileSettingForm(forms.ModelForm):
    firstname = forms.CharField(max_length=30, required=False)
    lastname = forms.CharField(max_length=30, required=False)
    # bio = forms.CharField(max_length=250, widget=forms.Textarea, required=False)
    # gender = forms.ChoiceField(choices=(('undefined', 'undefined'), ('male', 'male'), ('female', 'female')))
    class Meta:
        model = models.Account
        fields = ['bio', 'gender', 'profile_picture']

class CourseRegisterForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__'
