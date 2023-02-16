from typing import List

import stripe
from django.conf import settings

from main.models import Item, Order


def get_items_from_order(order: Order) -> List[Item]:
    return order.items.all()


def get_stripe_json_from_item(item: Item) -> dict:

    return {
        "price_data": {
        "currency": "usd",
        "product_data": {
                "name": item.name,
                "description": item.description
            },
            "unit_amount": int(item.price * 100)
        },
        "quantity": 1
    }


def get_stripe_session(id: int, obj_type: str) -> stripe.checkout.Session:
    if obj_type == "item":
        obj = Item.objects.get(id=id)
        line_items = [get_stripe_json_from_item(obj)]
    elif obj_type == "order":
        obj = Order.objects.get(id=id)
        line_items = [get_stripe_json_from_item(item) 
                    for item in get_items_from_order(obj)]


    stripe.api_key = settings.STRIPE_SECRET_KEY

    return stripe.checkout.Session.create(
        line_items=line_items,
        mode="payment",
        success_url=f"http://localhost:8000/item/{obj.id}/success",
        cancel_url=f"http://localhost:8000/item/{obj.id}/cancel"
    )
