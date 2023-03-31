from django import forms

from reviews.models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=100, error_messages={
#         "required": "Your name is required",
#         "max_length": "Please enter shorter name!",
#     })
#     review_text = forms.CharField(label="Your feedback", max_length=200, widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ['user_name', 'review_text', 'rating']
        fields = '__all__'
        # exclude = ['user_name', 'review_text', 'rating']
        labels = {
            'user_name': 'Your name',
            'review_text': 'Your feedback',
            'rating': 'Your rating'
        }
        error_messages = {
            'user_name': {
                'required': 'Your name is required',
                'max_length': 'Please enter shorter name'
                          }
        }
