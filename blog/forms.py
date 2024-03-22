from django import forms
from .models import Article, Profile, Comment

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'description',
            'photo',
            'category'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок статьи'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание статьи'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            })
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username ...'
                               }))

    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Password ...'
                               }))


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username ...'
                               }))

    first_name = forms.CharField(label="Ваше имя",
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'First name ...'
                                 }))

    last_name = forms.CharField(label="Ваша фамилия",
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Last name ...'
                                }))

    email = forms.EmailField(label="Ваша почта",
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Your email ...'
                             }))
    password1 = forms.CharField(label="Придумайте пароль",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password ...'
                                }))
    password2 = forms.CharField(label="Подтвердите пароль",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password ...'
                                }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')


class UserForm(forms.ModelForm):
    username = forms.CharField(label="Имя пользователя",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username ...'
                               }))

    first_name = forms.CharField(label="Ваше имя",
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'First name ...'
                                 }))

    last_name = forms.CharField(label="Ваша фамилия",
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Last name ...'
                                }))

    email = forms.EmailField(label="Ваша почта",
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Your email ...'
                             }))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'mobile',
                  'address', 'job',
                  'image')

        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            'job': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Профессия'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )

        widgets = {
            'text': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Напишите ваш коммент",
                "rows": 5
            })
        }
