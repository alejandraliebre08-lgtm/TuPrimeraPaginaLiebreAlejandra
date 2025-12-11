from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cliente', views.cliente, name='cliente'),
    path('producto', views.producto, name='producto'),
    path('pedido', views.pedido, name='pedido'),
    path('carrito', views.carrito, name='carrito'),
    path('clienteFormulario', views.clienteFormulario, name='clienteFormulario'),
    path("buscarClienteFormulario/", views.buscarClienteFormulario, name="buscarClienteFormulario"),
]




