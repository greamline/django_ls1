from django import forms
from authapp.models import User
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings




class UserCreateForm(UserCreationForm):
    # email = forms.EmailField(label='email',widget=forms.EmailField(attrs={'class':'form-control','placeholder':'email'}))
    # first_name = forms.CharField(label='first_name', widget=forms.CharField(attrs={'class':'form-control','placeholder':'Имя'}))
    # last_name = forms.CharField(label='Фамилия', widget=forms.CharField(attrs={'class':'form-control','placeholder':'Фамилия'}))
    # password1 = forms.PasswordInput(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Пароль'}))
    # password2 = forms.PasswordInput(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Подтвердждение пароля'}))
    # avatar = forms.ImageField(label='Аватарочка', error_messages = {'invalid':"Image files only"}, widget=forms.ImageField(attrs={'class': 'form-control','placeholder':'avatar'}))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name','birth_date','avatar','bio')
        widgets = {
            'avatar': forms.FileInput(),
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}, format='%d-%m-%Y'),
        }


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)




class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = ('password1','password2','password','last_login','is_superuser','is_staff','groups','rights','is_active','user_permissions','email')
        widgets = {
            'avatar': forms.FileInput(),
            'birth_date':forms.widgets.DateInput(attrs={'type': 'date'}, format='%d-%m-%Y'),
        }


