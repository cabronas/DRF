from django.db.migrations import serializer
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from REST.models import Product
from REST.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def get_prod(request):
    if request.method != 'POST':
        prod = Product.objects.all()
        ser = ProductSerializer(prod, many=True)
        return Response(ser.data)
    else:
        ser = ProductSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
def get_prodit(request, pid):
    prod = Product.objects.filter(id=pid)
    if request.method == 'GET':
        ser = ProductSerializer(prod, many=True)
        return Response(ser.data)
    elif request.method == 'PUT':
        ser = ProductSerializer(prod, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=200)
    else:
        prod.delete()
        return Response(status=200)


# @api_view(['POST'])
# def make_prod(request, name,price,count,comment):
# prod = Product.objects.get(id=pid)
# ser = ProductSerializer(prod, many=True)
# return Response(ser.data)

class Products(APIView):
    def get(self, request):
        prod = Product.objects.all()
        ser = ProductSerializer(prod, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = ProductSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)


class ProductDetail(APIView):
    def get(self, request, pid):
        prod = Product.objects.filter(id=pid)
        if request.method == 'GET':
            ser = ProductSerializer(prod, many=True)
            return Response(ser.data)

    def post(self, request, pid):
        prod = Product.objects.filter(id=pid)
        ser = ProductSerializer(prod, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=200)
        else:
            return Response(status=409)

    def delete(self, request, pid):
        prod = Product.objects.filter(id=pid)
        prod.delete()
        return Response(status=200)


class ProductsJR(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super(Product, self).get_queryset()
        queryset = queryset.filter(visible=True)
        return queryset


class ProductsJRDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductS(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductSDetail(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
