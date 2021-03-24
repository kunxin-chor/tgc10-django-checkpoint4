from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import ReviewForm
from .models import Review


def show_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index-template.html', {
        'reviews': reviews
    })

# Create your views here.


def create_review(request):
    if request.method == "POST":
        # first argument is filling in whatever the user provided via
        # the HTML form
        form = ReviewForm(request.POST)

        # check if the form has no errors
        if form.is_valid():
            # create the Review model from the form,
            # but don't save to the database yet (commit=False)
            review = form.save(commit=False)
            # request.user will refer to the currently logged in user
            review.owner = request.user
            review.save()
            messages.success(request, "New review has been added")
            return redirect(reverse(show_reviews))
    else:
        # create a new instance of ReviewForm
        create_form = ReviewForm()

        return render(request, 'reviews/create-template.html', {
            'form': create_form
        })