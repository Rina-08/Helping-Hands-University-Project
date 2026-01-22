from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('donate/', views.donate, name='donate'),
    path('request-donation/', views.request_donation, name='request_donation'),
    path('campaigns/', views.campaigns, name='campaigns'),
    path('request-campaign/', views.request_campaign, name='request_campaign'),
    path('feedback/', views.feedback, name='feedback'),
    path('help/', views.help_page, name='help'),
]
