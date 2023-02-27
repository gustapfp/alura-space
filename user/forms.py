from django import forms

class LoginForms(forms.Form):
    name_login = forms.CharField(
        label= "Nome do usuario",
        required = True,
        max_length = 100,
    )
    user_password = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput()
    )

class RegisterForms(forms.Form):
    name_login = forms.CharField(
        label= "Nome do usuario",
        required = True,
        max_length = 100,
    )
    email = forms.EmailField(
        label="Email", 
        required = True,
    )
    user_password_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput()
    )
    user_password_2 = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput()
    )