from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ReviewForm
from .models import Review


# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {
            'form': form
        })

    def post(self, request):
            # existing_model = Review.objects.get(pk=1)
            # form = ReviewForm(request.POST or None, instance=existing_model)
            form = ReviewForm(request.POST or None)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/thank-you')

            return render(request, 'reviews/review.html', {
                'form': form
            })


def thank_you(request):
    return render(request, 'reviews/thank_you.html')