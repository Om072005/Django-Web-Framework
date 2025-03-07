from django.shortcuts import render
from tradingbotweb.models import CurrencyBalance, ExchangeGoal
# Create your views here.
def index(request):

    last_balance= CurrencyBalance.objects.order_by('-created_at').first()
    exchange_goal = last_balance.exchange_goal.first()

    context = {
        'last_balance' : last_balance,
        'exchange_goal' : exchange_goal
    }

    return render(request,'home.html', context)