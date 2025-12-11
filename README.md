# TuPrimeraPaginaLiebre  
Proyecto Final – Tercera Entrega de Django  
Diplomatura en Python – Coderhouse  
Alumna: **Alejandra Liebre**

---

## 📌 Descripción del Proyecto

Este proyecto es una aplicación web creada con **Django**, siguiendo el patrón **MVT (Model–View–Template)**.  
Incluye:

- Herencia de plantillas HTML  
- Tres modelos: Cliente, Producto y Pedido  
- Formularios para cargar datos en la base de datos  
- Un formulario para buscar clientes por apellido  
- Navegación entre páginas usando enlaces y plantillas extendidas  

---

## 🧭 Orden recomendado para probar la aplicación

A continuación se detalla el orden recomendado para probar la web y la ubicación de cada funcionalidad solicitada.

### 1️⃣ Ingreso al sitio
Ingresar a:
```
http://127.0.0.1:8000/
```
Desde la página de **inicio** se accede al menú principal con todas las secciones.

---

### 2️⃣ Crear un nuevo cliente
Ruta desde el menú: **nuevo cliente**  
o:
```
/clienteFormulario
```
Funcionalidad:
- Completar el formulario **ClienteFormulario**
- Guardar el cliente en la base  
Luego puede verificarse en la lista de clientes.

---

### 3️⃣ Ver lista de clientes
Ruta desde el menú: **cliente**  
o:
```
/cliente
```
Funcionalidad:
- Mostrar todos los clientes registrados  

---

### 4️⃣ Cargar un nuevo producto
Ruta desde el menú: **producto**  
o:
```
/producto
```
Funcionalidad:
- Completar el formulario **ProductoFormulario**
- Guardar productos en la base de datos  

---

### 5️⃣ Registrar un pedido
Ruta desde el menú: **pedido**  
o:
```
/pedido
```
Funcionalidad:
- Crear pedidos vinculando cliente y producto  
- Ver listado de pedidos creados  

---

### 6️⃣ Buscar un cliente
Ruta desde el menú: **buscar cliente**  
o:
```
/buscar-cliente
```
Funcionalidad:
- Completar formulario de búsqueda (GET)
- Buscar clientes por apellido  
- Mostrar coincidencias o mensaje sin resultados  

---

## 📍 Ubicación de funcionalidades en el proyecto

### ✔ Modelos (models.py)
```
AppCoder/models.py
```
Incluye:
- Cliente  
- Producto  
- Pedido  

---

### ✔ Formularios (forms.py)
```
AppCoder/forms.py
```
Incluye:
- ClienteFormulario  
- ProductoFormulario  
- PedidoFormulario  
- BuscarClienteFormulario  

---

### ✔ Vistas (views.py)
```
AppCoder/views.py
```
Incluye:
- Lógica de inicio  
- Listados  
- Formularios  
- Búsqueda de clientes  

---

### ✔ Templates (HTML)
```
AppCoder/templates/AppCoder/
```
Incluye:
- base.html  
- inicio.html  
- cliente.html  
- clienteFormulario.html  
- producto.html  
- pedido.html  
- buscarCliente.html  

---

## ▶️ Cómo ejecutar el proyecto localmente

1. Clonar el repositorio:
```
git clone https://github.com/tu-usuario/TuPrimeraPaginaLiebre.git
cd TuPrimeraPaginaLiebre
```

2. Crear entorno virtual (opcional):
```
python -m venv venv
venv\Scripts\activate
```

3. Instalar dependencias:
```
pip install django
```

4. Aplicar migraciones:
```
python manage.py migrate
```

5. Ejecutar servidor:
```
python manage.py runserver
```

Ingresar en:
```
http://127.0.0.1:8000/
```

---

## ✔️ Conclusión

Este proyecto cumple con todos los requisitos de la Tercera Entrega:

- Herencia de plantillas  
- Tres modelos  
- Formularios para carga de datos  
- Formulario de búsqueda  
- Proyecto subido a GitHub  
- README explicativo indicando orden y ubicación de funcionalidades  


