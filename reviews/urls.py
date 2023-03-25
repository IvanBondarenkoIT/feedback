from django.urls import path, include

from . import views
from .views import review

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('review/', views.review),
    path('', review),
]
