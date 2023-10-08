APP INVENTARIO

La app de inventario del sistema repapp (REPuestos APP) fue desarrollado con el framework Django para un distribuidor de auto partes

La app de inventario se tienen 4 tablas:

Categoria

Producto

Orden

OrdenProducto

Una Categoria puede tener varios Productos.

Un Producto puede tener varios OrdenesProductos.

Una Orden puede tener varias OrdenesProductos.

La app de inventario tiene las siguientes API genericas:

GET, POST inventario/categorias/

GET/id, PUT, DELETE inventario/categorias/id/

GET, POST inventario/productos/

GET/id, PUT, DELETE inventario/productos/id>/

GET, POST inventario/ordenes/

GET/id, PUT, DELETE inventario/ordenes/id/

GET, POST inventario/ordenproductos/

GET/id, PUT, DELETE inventario/ordenproductos/id/

La app de inventario valida los siguientes campo de la tabla Categoria y Producto:

valida que el campo nombre de la tabla Categoria pueda recibir solo texto

valida que el campo descripcion de la tabla Producto pueda recibir solo texto

valida que el campo cantidad de la tabla OrdenProducto reciba cantindad menor o igual a 100

La app de invetario tiene la siguiente ruta persoanlizada que permite leer la cantidad de registros de la tabla Categoria

GET inventario/ categorias/cantidad/

Los integrantes que participaron en el desarrollo de la app de inventario son:

Alejandro

Gabriel Lavagen

Marin Fernandez

Victor Flores
