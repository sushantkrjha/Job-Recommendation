from django.urls import path
from .views import JobRecommendationView

urlpatterns = [
    path('recommend-jobs/', JobRecommendationView.as_view(), name='recommend-jobs'),
]
