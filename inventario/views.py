from rest_framework import generics
from .models import Categoria, Producto, Orden, OrdenProducto
from .serializers import CategoriaSerializer, ProductoSerializer, OrdenSerializer, OrdenProductoSerializer

# Vistas para la API de Categorías
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Vistas para la API de Productos
class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Vistas para la API de Órdenes
class OrdenListCreateView(generics.ListCreateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class OrdenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

# Vistas para la API de Órdenes de Productos
class OrdenProductoListCreateView(generics.ListCreateAPIView):
    queryset = OrdenProducto.objects.all()
    serializer_class = OrdenProductoSerializer

class OrdenProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrdenProducto.objects.all()
    serializer_class = OrdenProductoSerializer