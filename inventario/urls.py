from django.urls import path
from . import views

urlpatterns = [
    # URLs para Categorías
    path('categorias/', views.CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),

    # URLs para Productos
    path('productos/', views.ProductoListCreateView.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto-detail'),

    # URLs para Órdenes
    path('ordenes/', views.OrdenListCreateView.as_view(), name='orden-list-create'),
    path('ordenes/<int:pk>/', views.OrdenDetailView.as_view(), name='orden-detail'),

    # URLs para Órdenes de Productos
    path('ordenproductos/', views.OrdenProductoListCreateView.as_view(), name='ordenproducto-list-create'),
    path('ordenproductos/<int:pk>/', views.OrdenProductoDetailView.as_view(), name='ordenproducto-detail'),

    # URLs para Cantidad de Categorias (API personalizada)
    path('categorias/cantidad/', views.categoria_count, name='categorias_cantidad'),
]