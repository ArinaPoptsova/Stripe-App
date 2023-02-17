import json

from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
import stripe
from django.http import JsonResponse, HttpResponse
from .models import Item
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentView(View):
    def get(self, request, *args, **kwargs):
        try:
            item = Item.objects.get(id=self.kwargs['pk'])
            # data = json.loads(request.body)
            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount=item.price,
                currency=item.currency,
                automatic_payment_methods={
                    'enabled': True,
                },
            )
            return JsonResponse({
                    'clientSecret': intent['client_secret']
                })
        except Exception as e:
            return JsonResponse({'error': str(e)})


class ItemView(DetailView):
    model = Item
    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context
