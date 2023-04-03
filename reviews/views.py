from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from pyexpat import model

from .forms import ReviewForm
from .models import Review


# Create your views here.
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = "/thank_you.html"

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, 'reviews/review.html', {
    #         'form': form
    #     })

    # def post(self, request):
    #         # existing_model = Review.objects.get(pk=1)
    #         # form = ReviewForm(request.POST or None, instance=existing_model)
    #         form = ReviewForm(request.POST or None)
    #
    #         if form.is_valid():
    #             form.save()
    #             return HttpResponseRedirect('/thank-you')
    #
    #         return render(request, 'reviews/review.html', {
    #             'form': form
    #         })


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=2)
        return data

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context['reviews'] = reviews
    #     return context


class ReviewDetailView(DetailView):
    template_name = 'reviews/review_details.html'
    model = Review

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_review = Review.objects.get(pk=review_id)
    #     context['review'] = selected_review
    #     return context
