from django.urls import path
from .views import (BigCategoryListCreateView,BigCategoryDetailView,)

urlpatterns = [
    path("", BigCategoryListCreateView.as_view(), name="category-list"),
    path("<int:pk>/", BigCategoryDetailView.as_view(), name="category-detail"),
]