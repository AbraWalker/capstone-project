from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import ReviewForm
# Create your views here.
class ReviewList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "index.html"

def review_details(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    review_form = ReviewForm()
    return render(
        request, "reviews_list.html", 
        {"post": post,
         "review_form": review_form
        },
        )

def home_view(request):
    #renders homepage
    return render(request, 'index.html')

def guidelines_view(request):
    #renders guidelines
    return render(request, 'guidelines.html')