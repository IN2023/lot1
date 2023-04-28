from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Good, Brand


class RegisterUserForm(UserCreationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput)  #  на екрані буде видно лише рядок вводу, без зайвих підсказок
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)  #  на екрані буде видно лише рядок вводу, без зайвих підсказок
    password2 = forms.CharField(label="Repeat the password", widget=forms.PasswordInput)  #  на екрані буде видно лише рядок вводу, без зайвих підсказок

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", )


class GoodsForm(forms.ModelForm):
    icon = forms.ImageField(label="Image", widget=forms.FileInput)
    brand = forms.CharField(label="Brand", widget=forms.TextInput)
    title = forms.CharField(label="Title", widget=forms.TextInput)
    number_of_servings = forms.CharField(label="Brand", widget=forms.NumberInput)
    price = forms.FloatField(label="Price", widget=forms.NumberInput)

    class Meta:
        model = Good
        fields = ("icon", "brand", "title", "number_of_servings", "price")


class BrandsForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ("title", )
