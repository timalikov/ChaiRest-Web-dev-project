from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

from models import Category, Furniture
from serializers import UserSerializer, CategorySerializer, FurnitureSerializer, OrderSerializer
from rest_framework.pagination import LimitOffsetPagination


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Category.objects.all()

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        return Category.objects.filter(id=id)



# class CategoryFurnitureList(generics.ListAPIView):
#     serializer_class = FurnitureSerializer
#     permission_classes = (AllowAny, )
#
#     def get_queryset(self):
#         category_id = self.kwargs['id']
#         Category = get_object_or_404(Category, id=category_id)
#         return category.vacancies.all()


class FurnitureListView(generics.ListCreateAPIView):
    serializer_class = FurnitureSerializer
    permission_classes = (AllowAny, )
    queryset = Furniture.objects.all()


class FurnitureDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FurnitureSerializer
    permission_classes = (AllowAny, )
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        return Furniture.objects.filter(id=id)

