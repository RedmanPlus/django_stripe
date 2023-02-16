from django.urls import path

from main import views

urlpatterns = [
    path(
        "config/", views.ConfigAPIView.as_view(), name="config"
    ),
    path(
        "buy/<int:id>", views.BuyItemAPIView.as_view(), name="buy"
    ),
    path(
        "item/<str:pk>", views.ItemView.as_view(), name="item"
    ),
    path(
        "order/", views.CreateOrderAPIView.as_view(), name="create-order"
    ),
    path(
        "buy-order/<int:id>", views.ExecuteOrderAPIView.as_view(), name="execute-order"
    ),
    path(
        "order/<str:pk>", views.OrderView.as_view(), name="order"
    ),
]
