from typing import ItemsView
from django.urls import path
from .views import *


urlpatterns = [
    path("store/", StoreView.as_view()),
    path("store/<int:id>", get_store, name="get_store"),
    path("store/<int:id>/orders", get_store, name="get_store"),
    path("order", OrderView.as_view()),
    path("order/<int:id>", get_order, name="get_store"),
    path("order/<int:id>/", OrderView.as_view(), name="get_store"),
    path("order/<int:id>/item", get_order_item, name="get_store"),
    path("item/", ItemView.as_view(), name="create item"),
    path("item/<int:id>", get_item, name="get_item"),
    path("item/<int:id>/", ItemView.as_view(), name="get_item"),
]
