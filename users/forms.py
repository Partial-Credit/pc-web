from django import forms
from .models import Member

class FullMemberForm(forms.ModelForm):
    class Meta:
        model = Member

        # Add CSS class 'form-control' to all fields to allow styling
        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.NumberInput(attrs={'class': 'form-control'}),
            'voice_part': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control date-picker'}),
            'major': forms.TextInput(attrs={'class': 'form-control date-picker'}),
            'class_year': forms.TextInput(attrs={'class': 'form-control date-picker'}),
            'current_member': forms.TextInput(attrs={'class': 'form-control date-picker'}),
        }

        fields = [
            "first_name",
            "last_name",
            "bio",
            "nickname",
            "voice_part",
            "position",
            "major",
            "class_year",
            "current_member",
        ]

class MemberForm(forms.ModelForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    bio = forms.Textarea()
    nickname = forms.CharField()
    voice_part = forms.Select()
    major = forms.CharField()
    class_year = forms.NumberInput()
    profile = forms.FileInput()
    other_email = forms.EmailField()

    class Meta:
        model = Member

        # Add CSS class 'form-control' to all fields to allow styling
        # widgets = {
        #     'bio': forms.TextInput(attrs={'class': 'form-control'}),
        #     'nickname': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'voice_part': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        #     'major': forms.TextInput(attrs={'class': 'form-control date-picker'}),
        #     'class_year': forms.TextInput(attrs={'class': 'form-control date-picker'}),
        # }

        fields = [
            "first_name",
            "last_name",
            "bio",
            "nickname",
            "voice_part",
            "major",
            "class_year",
            "profile",
            "other_email",
            "current_member",
        ]
