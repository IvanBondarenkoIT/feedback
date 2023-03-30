from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=100, error_messages={
        "required": "Your name is required",
        "max_length": "Please enter shorter name!",

    })