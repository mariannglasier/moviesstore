from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.models import Order, Item
from django.db.models import Sum
def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    return render(request, 'home/index.html', {'template_data': template_data})
def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html', {'template_data': template_data})

@login_required
def subscription(request):
    template_data = {}
    template_data['title'] = 'Subscription'

    user = request.user

    total_spent = Order.objects.filter(user=user).aggregate(total=Sum('total'))['total'] or 0

    if total_spent < 15:
        subscription_level = 'Basic'
    elif 15 <= total_spent < 30:
        subscription_level = 'Medium'
    else:
        subscription_level = 'Premium'

    template_data['total_spent'] = total_spent
    template_data['subscription_level'] = subscription_level
    
    return render(request, 'home/subscription.html', {'template_data': template_data})

# Create your views here.
