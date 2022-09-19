from django.shortcuts import render

from django.http.response import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view

def index(request):
    return render(request,'index.html')

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        userid = request.query_params.get('userid', None)
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def user_create(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT']) #or we can use patch also
def user_update(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def user_delete(request, pk):
    try:
        user = User.objects.get(userid=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        user.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def product_create(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def product_delete(request, pk):
    try:
        product = Product.objects.get(productid=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        product.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'POST'])
def seller_list(request):
    if request.method == 'GET':
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SellerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['PUT'])
def seller_create(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SellerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def seller_delete(request, pk):
    try:
        seller = Seller.objects.get(sellerid=pk)
    except Seller.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        seller.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'POST'])
def product_seller_list(request):
    if request.method == 'GET':
        product_sellers = ProductSeller.objects.all()
        serializer = ProductSellerSerializer(product_sellers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSellerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def product_seller_create(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSellerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def product_seller_delete(request, pk):
    try:
        product_seller = ProductSeller.objects.get(productsellerid=pk)
    except ProductSeller.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        product_seller.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'POST'])
def address_list(request):
    if request.method == 'GET':
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def address_create(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def address_delete(request, pk):
    try:
        address = Address.objects.get(addressid=pk)
    except Address.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        address.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def order_create(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def order_delete(request, pk):
    try:
        order = Order.objects.get(orderid=pk)
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        order.delete()
        return HttpResponse(status=204)

@api_view(['PUT'])
def order_update(request, pk):
    try:
        order = Order.objects.get(orderid=pk)
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def order_seller_list(request, pk):
    if request.method == 'GET':
        orders = Order.objects.filter(sellerid=pk)
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def order_user_list(request, pk):
    if request.method == 'GET':
        orders = Order.objects.filter(userid=pk)
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)
