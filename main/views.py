from django.conf import settings
from django.views.generic import DetailView

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from main.models import Item, Order
from main.BL.session_creation import get_stripe_session
from main.serializers import OrderSerializer


class ConfigAPIView(APIView):

    def get(self, request, *args, **kwargs):

        return Response(
            {
                "key": settings.STRIPE_PUBLISH_KEY
            },
            status=status.HTTP_200_OK
        )


class BuyItemAPIView(APIView):

    def get(self, request, *args, **kwargs):

        id = self.kwargs.get("id")
        session = get_stripe_session(id, "item")

        return Response({"id": session.id}, status=status.HTTP_200_OK)


class CreateOrderAPIView(CreateAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ExecuteOrderAPIView(APIView):

    def get(self, request, *args, **kwargs):

        id = self.kwargs.get("id")
        session = get_stripe_session(id, "order")

        return Response({"id": session.id}, status=status.HTTP_200_OK)


class ItemView(DetailView):

    model = Item


class OrderView(DetailView):

    model = Order
