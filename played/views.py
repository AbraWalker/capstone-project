from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
# Create your views here.
class ReviewList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "index.html"

def review_details(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    return render(request, "played/review_list.html", {"review": post},)