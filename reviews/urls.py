from django.urls import path, include

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('review/', views.review),
    path('', views.ReviewView.as_view()),
    path('thank-you', views.ThankYouView.as_view()),
    path('reviews', views.ReviewsListView.as_view()),
    path('reviews/favorite', views.AddFavoriteView.as_view()),
    path('review/<int:pk>', views.ReviewDetailView.as_view()),
]
