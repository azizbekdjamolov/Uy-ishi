from django.urls import path
from .views import (CategoryListCreateView,CategoryDetailView)

urlpatterns = [
    path("", CategoryListCreateView.as_view(), name="subcategory-list"),
    path("<int:pk>/", CategoryDetailView.as_view(), name="subcategory-detail"),
]