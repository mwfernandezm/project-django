API REST CON DJANGO

Es una app inventario del sistema repapp (APP de Repuestos) desarrollado con el framework Django para una tienda o distribuidor de auto partes

La app inventario se tienen 4 tablas:

Categoria,
Producto,
Orden,
OrdenProducto

Una Categoria puede tener varios Productos

Un Producto puede tener varios OrdenesProductos

Una Orden puede tener varias OrdenesProductos

La app inventario tiene las siguientes rutas:

API genericas:

GET, POST inventario/categorias/
GET/<int:pk, PUT, DELETE inventario/categorias/<int:pk>/

GET, POST inventario/productos/
GET/<int:pk, PUT, DELETE inventario/productos/<int:pk>/

GET, POST inventario/ordenes/
GET/<int:pk, PUT, DELETE inventario/ordenes/<int:pk>/

GET, POST inventario/ordenproductos/
GET/<int:pk, PUT, DELETE inventario/ordenproductos/<int:pk>/

La app Inventario valida el campo:

valida que el campo nombre de la tabla Categorias pueda recibir solo texto

valida que el campo descripcion de la tabla Producto pueda recibir solo texto

valida que el campo cantidad de la tabal OrdenProducto reciba cantindad menor o igual a 100

API customizada que permite leer la cantidad de registros de la tabla Categoria

GET inventario/ categorias/cantidad/

Los integrantes que participaron en el desarrollo de la app inventarios son:

Alejandro

Gabriel Lavagen

Marin Fernandez

Victor Flores
