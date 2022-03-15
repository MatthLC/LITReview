"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
import authentication.views
import flux.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('home/', flux.views.home, name='home'),
    path('new_ticket/', flux.views.create_ticket, name='new_ticket'),
    path('post/', flux.views.show_posts, name='view_post'),
    path('post/<int:ticket_id>/edit', flux.views.edit_post, name='edit_post'),
    path('review/<int:review_id>/edit', flux.views.edit_review, name='edit_review'),
    path('review/', flux.views.create_review, name='new_review'),
    path('follow/', flux.views.follow_users, name='follow'),
    path('review/<int:ticket_id>/new', flux.views.create_review_from_ticket, name='review_from_ticket'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
