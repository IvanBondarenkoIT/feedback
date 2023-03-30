from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=100, error_messages={
        "required": "Your name is required",
        "max_length": "Please enter shorter name!",
    })
    review_text = forms.CharField(label="Your feedback", max_length=200, widget=forms.Textarea)
    rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)
