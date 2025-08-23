from . import views
from django.urls import path
from .views import home_view, guidelines_view, review_details

urlpatterns = [
    path('', home_view, name="home"),
    path('guidelines/', guidelines_view, name="guidelines"),
    path('<slug:slug>/', views.review_details, name="review_details"),
]