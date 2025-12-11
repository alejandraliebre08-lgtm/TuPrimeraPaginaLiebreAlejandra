from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Cliente
from .forms import ClienteFormulario
from .forms import BuscarClienteFormulario

def inicio(request):
    return render(request, "AppCoder/inicio.html")
    
def cliente(request):
    clientes = Cliente.objects.all()
    contexto = {"clientes": clientes}
    return render(request, "AppCoder/cliente.html", contexto)

def producto(request):
    return render(request, "AppCoder/producto.html")


def carrito(request):
    return render(request, "AppCoder/carrito.html")


def pedido(request):
    return render(request, "AppCoder/pedido.html")


def clienteFormulario(request):
    if request.method == "POST":
        miFormulario = ClienteFormulario(request.POST)   

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            cliente = Cliente(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion["email"],
                telefono=informacion["telefono"],
            )
            cliente.save()

            return redirect("cliente")   

    else:
        miFormulario = ClienteFormulario()   

    return render(
        request,
        "AppCoder/clienteFormulario.html",
        {"miFormulario": miFormulario}
    )

def buscarClienteFormulario(request):
    formulario = BuscarClienteFormulario(request.GET or None)
    resultados = None

    if formulario.is_valid():
        apellido = formulario.cleaned_data.get("apellido")
        if apellido:
            resultados = Cliente.objects.filter(apellido__icontains=apellido)

    return render(request, "AppCoder/buscar_cliente.html", {
        "formulario": formulario,
        "resultados": resultados,
    })
   
