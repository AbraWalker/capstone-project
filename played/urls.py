from . import views
from django.urls import path
from played.views import home_view, guidelines_view, submit_list, ReviewList, delete_review, edit_review

urlpatterns = [

    path('', home_view, name="home"),
    path('guidelines/', guidelines_view, name="guidelines"),
    path('reviews/', ReviewList.as_view(), name="reviews"),
    path('submit/', submit_list, name="submit"),
    path('reviews/delete/<int:id>', views.delete_review, name="delete"),
    path('reviews/edit/<int:id>', edit_review, name="edit")
]