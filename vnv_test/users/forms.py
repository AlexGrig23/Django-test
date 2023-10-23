from django import forms
from .models import User, Group


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['user_name', 'group']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'})
        }


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }
