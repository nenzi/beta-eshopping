from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import views
from .models import *
from .serializers import *
from .response import CustomResponse as res

# Create your views here.


class StoreView(views.APIView):
    def get(self, request):
        store = Store.objects.all()
        serializer = StoreSerializer(store, many=True)
        return res(serializer.data).response()

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        store = Store.objects.create(**data)
        store.save()
        return res(serializer.data).response()


@api_view(["GET"])
def get_store(request, id):
    store = get_object_or_404(Store, pk=id)
    serializer = StoreSerializer(store)
    return res(serializer.data).response()


@api_view(["GET"])
def get_store_orders(request, id):
    store = get_object_or_404(Store, pk=id)
    orders = Order.objects.get(store=store)
    serializer = OrderSerializer(orders, many=True)
    return res(serializer.data).response()


class OrderView(views.APIView):
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return res(serializer.data).response()

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        store = get_object_or_404(Store, id=data["store"])
        data["store"] = store
        order = Order.objects.create(**data)
        order.save()
        return res(serializer.data).response()

    def delete(self, request, id):
        order = get_object_or_404(Order, id=id)
        order.status = "canceled"
        order.save()
        serializer = OrderSerializer(order)
        return res(serializer.data).response()


@api_view(["GET"])
def get_order(request, id):
    order = get_object_or_404(Order, pk=id)
    serializer = OrderSerializer(order)
    return res(serializer.data).response()


class ItemView(views.APIView):
    def get(self, request):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return res(serializer.data).response()

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        store = get_object_or_404(Store, id=data["store"])
        data["store"] = store
        item = Item.objects.create(**data)
        item.save()
        return res(serializer.data).response()

    def put(self, request, id):
        item = Item.objects.get(pk=id)
        item = ItemSerializer(item, data=request.data)
        item.is_valid(raise_exception=True)
        item.save()
        return res(item.data).response()


@api_view(["GET"])
def get_item(request, id):
    item = get_object_or_404(Order, pk=id)
    serializer = ItemSerializer(item)
    return res(serializer.data).response()


class OrderItemView(views.APIView):
    def post(self, request):
        serializer = OrderItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        order = get_object_or_404(Order, id=data["order"])
        item = get_object_or_404(Item, id=data["item"])
        data["item"] = item
        data["order"] = order
        order_item = OrderItem.objects.create(**data)
        order_item.save()
        return res(serializer.data).response()


@api_view(["GET"])
def get_order_item(request, id):
    order = get_object_or_404(Order, pk=id)
    order_item = OrderItem.objects.get(order=order)
    print(order_item)
    serializer = GetOrderItemSerializer(order_item)
    return res(serializer.data).response()
