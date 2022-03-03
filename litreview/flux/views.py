from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from itertools import chain
from . import forms
from . import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q

User = get_user_model()


# Create your views here.
@login_required
def follow_users(request):
    follow_form = forms.UserFollowsForm(instance=request.user)
    unfollow_form = forms.UnfollowForm()

    following = models.UserFollows.objects.filter(user=request.user)
    followed_by = models.UserFollows.objects.filter(followed_user=request.user)

    if request.method == 'POST':
        if 'follow_widget' in request.POST:

            follow_form = forms.UserFollowsForm(request.POST, instance=request.user)

            if follow_form.is_valid():
                try:
                    user_want_to_follow = User.objects.get(username=follow_form.cleaned_data['follow_form'])
                    follow = models.UserFollows(user=request.user, followed_user=user_want_to_follow)
                    follow.save()
                    return redirect('home')
                except ObjectDoesNotExist:
                    unknown_user = 'Utilisateur inconnu.'
                    return render(
                        request,
                        'flux/follow_users_form.html',
                        context={
                            'follow_form': follow_form,
                            'following': following,
                            'followed_by': followed_by,
                            'unfollow_form': unfollow_form,
                            'unknown_user': unknown_user
                        }
                    )

        if 'unfollow_widget' in request.POST:
            user_to_unfollow = get_object_or_404(models.UserFollows, id=request.POST.get('user_id'))
            user_to_unfollow.delete()
            return redirect('home')

    return render(
        request,
        'flux/follow_users_form.html',
        context={
            'follow_form': follow_form,
            'following': following,
            'followed_by': followed_by,
            'unfollow_form': unfollow_form,
        }
    )


@login_required
def home(request):
    print('===============')
    print(models.Ticket.objects.all())
    print('===============')
    followed = models.UserFollows.objects.filter(user=request.user).values_list('followed_user_id', flat=True)
    user_review = models.Review.objects.filter(user=request.user)
    user_ticket = models.Ticket.objects.filter(user=request.user)
    reviews_followed = models.Review.objects.filter(user__id__in=followed)
    tickets_followed = models.Ticket.objects.filter(user__id__in=followed)

    tickets_and_reviews = sorted(
        chain(user_ticket, user_review, tickets_followed, reviews_followed),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    tickets = sorted(
        chain(user_ticket, tickets_followed),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    all_reviews = []

    for ticket in tickets:
        my_ticket = models.Ticket.objects.get(id=ticket.id)
        any_review = my_ticket.ticketOf.all()
        if len(any_review) > 0:
            all_reviews.append(my_ticket)


    paginator = Paginator(tickets_and_reviews, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
 
    return render(
        request,
        'flux/home.html',
        context={
            'page_obj' : page_obj,
            'all_reviews': all_reviews
        }
    )


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')

    return render(request, 'flux/new_ticket.html', context={'form': form})


@login_required
def show_posts(request):
    widget_ticket_form = forms.WidgetTicketForm()
    widget_review_form = forms.WidgetReviewForm()
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)

    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    if request.method == 'POST':
        if 'widget_ticket' in request.POST:
            widget_ticket_form = forms.WidgetTicketForm(request.POST)
            if widget_ticket_form.is_valid():
                ticket = get_object_or_404(models.Ticket, id=request.POST.get('ticket_id'))
                ticket.delete()
                return redirect('home')

        if 'widget_review' in request.POST:
            widget_review_form = forms.WidgetReviewForm(request.POST)
            if widget_review_form.is_valid():
                review = get_object_or_404(models.Review, id=request.POST.get('review_id'))
                review.delete()
                return redirect('home')

    return render(
        request,
        'flux/post.html',
        context={
            'tickets_and_reviews': tickets_and_reviews,
            'widget_ticket_form': widget_ticket_form,
            'widget_review_form': widget_review_form
        }
    )


@login_required
def edit_post(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)

    if request.method == 'POST':
        edit_form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')

    return render(request, 'flux/edit_post.html', context={'edit_form': edit_form})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    ticket = get_object_or_404(models.Ticket, id=review.ticket_id)
    edit_review_form = forms.ReviewForm(instance=review)

    if request.method == 'POST':
        edit_form = forms.ReviewForm(request.POST, instance=review)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')
    return render(request, 'flux/edit_review.html', context={'ticket': ticket, 'edit_review_form': edit_review_form})


@login_required
def create_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()

    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('home')

    return render(
        request,
        'flux/new_review.html',
        context={'ticket_form': ticket_form, 'review_form': review_form}
    )


@login_required
def create_review_from_ticket(request, ticket_id):

    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review_form = forms.ReviewForm()

    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('home')

    return render(
        request,
        'flux/review_from_ticket.html',
        context={'ticket': ticket, 'review_form': review_form}
    )
