from django import forms
from . import models


class UserFollowsForm(forms.ModelForm):
    follow_widget = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    follow_form = forms.CharField(max_length=128, label='', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.UserFollows()
        fields = ['follow_form']
        widgets = {
            'follow_form': forms.TextInput(attrs={'class': 'form-control'})
        }


class UnfollowForm(forms.Form):
    unfollow_widget = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'rating': forms.RadioSelect(attrs={'class': 'd-flex form-check form-check-inline'}),
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control text-break'}),
        }


class WidgetTicketForm(forms.Form):
    widget_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class WidgetReviewForm(forms.Form):
    widget_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class DeletePostForm(forms.Form):
    delete_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
