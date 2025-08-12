from django import forms
from django.core.validators import EmailValidator, MinLengthValidator, RegexValidator

class RegisterForm(forms.Form):
    username= forms.CharField(label="Username", validators=[
        MinLengthValidator(4,message="At least 4 letters required"),
        RegexValidator(r'^[a-zA-Z0-9_]+$', message="Only letters, numbers, and underscores allowed")
        ])
    email= forms.EmailField(label="Email Address", validators=[
        EmailValidator(message="Enter a valid Email Address")
    ])
    password= forms.CharField(label="Password", widget=forms.PasswordInput,  validators=[MinLengthValidator(8, message="Password must be at least 8 characters")])
    confirm_password= forms.CharField(widget=forms.PasswordInput,label="Confirm Password",  validators=[MinLengthValidator(8, message="Password must be at least 8 characters")])
    def clean(self):
        cleaned_data=super().clean()
        p1=cleaned_data.get("password")
        p2=cleaned_data.get("confirm_password")
        if p1!=p2:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data