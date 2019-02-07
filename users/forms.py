from django import forms
from .models import Member

class FullMemberForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    bio = forms.Textarea()
    nickname = forms.CharField()
    voice_part = forms.Select()
    major = forms.CharField()
    position = forms.Select()
    class_year = forms.NumberInput()
    profile = forms.FileInput()
    other_email = forms.EmailField()
    username = forms.CharField()

    class Meta:
        model = Member

        fields = [
            "first_name",
            "last_name",
            "username",
            "bio",
            "nickname",
            "major",
            "voice_part",
            "position",
            "class_year",
            "profile",
            "other_email",
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

        fields = [
            "first_name",
            "last_name",
            "bio",
            "nickname",
            "major",
            "voice_part",
            "class_year",
            "profile",
            "other_email",
            "current_member",
        ]
