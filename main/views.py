import stripe
from rest_framework.views import APIView


class BuyAPIView(APIView):

    def get(self, request, *args, **kwargs):

        id = self.kwargs.get("id")
        stripe_session_id = stripe.checkout.Session.create(

        )
        