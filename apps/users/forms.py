from django import forms
from django.core.exceptions import ValidationError
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control text-bg-dark'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control text-bg-dark'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control text-bg-dark'}),
            'email': forms.EmailInput(attrs={'class': 'form-control text-bg-dark'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control text-bg-dark', 'id': 'password_register'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está en uso")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Las contraseñas no coinciden")

        return cleaned_data

class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control text-bg-dark', 'id': 'email_login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control text-bg-dark', 'id': 'password_login'}))