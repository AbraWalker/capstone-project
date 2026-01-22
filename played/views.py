from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post #, Guide
from .forms import ReviewForm, GuideForm

# Create your views here.
class ReviewList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "review_list.html"
    context_object_name = 'review'
    paginate_by = 5

def submit_list(request):
    queryset = Post.objects.all().order_by("created_on")
    review = get_object_or_404(queryset)
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review submitted!')
        else:
            messages.add_message(request, messages.ERROR, 'Cannot submit review.')
    review_form = ReviewForm()
    return render(request, "review_submit.html",
        {
        "review_form": review_form,
        "review": review
        },
        )

def delete_review(request, id):
    review = get_object_or_404(Post, pk=id)
    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted.')
    else:
        messages.add_message(request, messages.ERROR, 'Cannot delete other user reviews.')
    return HttpResponseRedirect(reverse('reviews'))

def edit_review(request, id):
    review = get_object_or_404(Post, pk=id)
    review_form = ReviewForm(data=request.POST, instance=review)
    if review_form.is_valid() and review.author == request.user:
        review = review_form.save(commit=False)
        review.save()
        messages.add_message(request, messages.SUCCESS, 'Review updated.')
    else:
        messages.add_message(request, messages.ERROR, 'Cannot update review.')
    return HttpResponseRedirect(reverse('reviews'))


#def guides_view(request):
#    queryset = Guide.objects.all()
#   guides = get_object_or_404(queryset)
#   return render(request, "guide_list.html", {"guides": guides},)

def home_view(request):
    #renders homepage
    return render(request, 'index.html')

def guidelines_view(request):
    #renders guidelines
    return render(request, 'guidelines.html')
