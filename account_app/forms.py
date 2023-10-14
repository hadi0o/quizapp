from django import forms
from .models import SEX_CHOICES, Profile


class LoginForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'آدرس ایمیل'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))
    conf_pass = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'تایید رمز عبور'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'tel', 'sex', 'age', 'field_of_study', 'city', 'sleep_time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تلفن'}),
            'sex': forms.Select(attrs={'class': 'form-control', 'placeholder': 'جنسیت'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'سن'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رشته تحصیلی'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر'}),
            'sleep_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شب گذشته چند ساعت خوابیده اید'}),
        }
