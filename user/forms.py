from django import forms

class LoginForms(forms.Form):
    name_login = forms.CharField(
        label= "Nome do usuario",
        required = True,
        max_length = 100,
        widget=forms.TextInput(
            attrs= {
                'class' : 'form-control',
                'placeholder': 'Ex: João Silva'
            }
        )
    )
    user_password = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs= {
                'class' : 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

class RegisterForms(forms.Form):
    name_login = forms.CharField(
        label= "Nome do usuario",
        required = True,
        max_length = 100,
        widget=forms.TextInput(
            attrs= {
                'class' : 'form-control',
                'placeholder': 'Ex: João Silva'
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com',
            }
        )
    )
    user_password_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )
    user_password_2 = forms.CharField(
        label="Repita sua senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )