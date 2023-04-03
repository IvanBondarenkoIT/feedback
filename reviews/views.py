from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
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


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works!"
        return context


class ReviewsListView(TemplateView):
    template_name = 'reviews/review_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews
        return context


class ReviewDetailView(TemplateView):
    template_name = 'reviews/review_details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        context['review'] = selected_review
        return context
