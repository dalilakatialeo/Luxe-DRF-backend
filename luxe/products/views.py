from django.http import Http404
from rest_framework import status, permissions
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer

class Recommendation(APIVIew):
    def post(self, request):
        user_recommendation = Recommendation.objects.filter(user =request.user).first()
        if user_recommendation:
            return Response(dict(answer= user_recommendation))
        answer_questions = request.body 
        recommendation = workout_recommendation(answer_questions)
        return Response(dict(answer=recommendation))

def workout_recommendation(answer_questions):
    #if statment logic stuff here
    return recommendation

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request): 
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProductDetail(APIView):
    def get_object(self, pk): 
        return Product.objects.get(pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        data = request.data
        serializer = ProductDetailSerializer(
            instance=product,
            data=data,
            partial=True
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                )
        print('here', serializer.is_valid(), serializer.errors, data)
        return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
