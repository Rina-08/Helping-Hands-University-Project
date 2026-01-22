from django.shortcuts import render

def home(request): return render(request, 'core/home.html')
def about(request): return render(request, 'core/about.html')
def blogs(request): return render(request, 'core/blogs.html')
def login_view(request): return render(request, 'core/login.html')
def signup(request): return render(request, 'core/signup.html')
def donate(request): return render(request, 'core/donate.html')
def request_donation(request): return render(request, 'core/request_donation.html')
def campaigns(request): return render(request, 'core/campaigns.html')
def request_campaign(request): return render(request, 'core/request_campaign.html')
def feedback(request): return render(request, 'core/feedback.html')
def help_page(request): return render(request, 'core/help.html')
