from django import forms
from .models import Comment, Profile, Blog
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post_date", "is_delete"]
        labels = {
            "text": "Your Message",
        }


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["passport"]


class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ["post_date", "author"]
