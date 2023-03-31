from django.urls import path, include

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('review/', views.review),
    path('', views.ReviewView.as_view()),
    path('thank-you', views.thank_you),
]
