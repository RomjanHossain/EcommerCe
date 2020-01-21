from django import forms
from django.contrib.auth import get_user_model


class ContactForm(forms.Form):
    Fullname = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={"placeholder": "Enter your name"}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={"placeholder": "Enter your Email"}))
    content = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={"placeholder": "Your message here..."}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['Fullname'].label = "Full Name"

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'gmail.com' not in email:
            raise forms.ValidationError("This is not gmail, bro")
        return email


class Loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


User = get_user_model()


class Registerform(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(label="Conform Password", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is Taken!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is Taken!")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password != password1:
            raise forms.ValidationError("Password should match, boy")
        return data
