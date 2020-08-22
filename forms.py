CART_AVAILABLE = False
CARRITO_ID = 0 #por defecto es 0, puesto que no existe al principio
CARRITO_LOCAL = []

class RegistroCarrito(Form):
#def __init__(self, id, id_carrito, id_producto, id_cantidad):
	self.id = id
	self.id_carrito = id_carrito
	self.id_producto = id_producto
	self.id_cantidad = id_cantidad

def agregarACarrito(id_producto, id_usuario, id_cantidad):
	if (CART_AVAILABLE):
		INSERT INTO carrito(usuario) VALUES (id_usuario);
		INSERT INTO carritoDetalle(id_carrito) values (CARRITO_ID, id_producto);
		CARRITO_LOCAL.append(RegistroCarrito(<id>, CARRITO_ID, id_producto, id_cantidad))
	else:
		CART_AVAILABLE = True
		INSERT INTO carrito(usuario) VALUES (id_usuario);
		CARRITO_ID = SELECT id FROM carrrito WHERE id = MAX(id) AND usuario = id_usuario
		INSERT INTO carritoDetalle(id_carrito) VALUES (CARRITO_ID, id_producto);
		CARRITO_LOCAL.append(RegistroCarrito(<id>, CARRITO_ID, id_producto, id_cantidad))

def eliminarDeCarrito(id_carritoDetalle):
	IF (CART_AVAILABLE):
		DELETE FROM carritoDetalle WHERE id = carritoDetalle;


def EliminarTodoCarrito(id_carrito):
	if(CART_AVAILABLE):
		DELETE FROM Carrito WHERE id = id_carrito;
		CART_AVAILABLE = False
		CARRITO_ID = 0

#Aca se muestran los datos que hay dentro del carrito
SELECT P.descripcion as "Producto", P.Precio as "Precio Unitario", count(*) as "Unidades" FROM CARRITO C INNER JOIN carritoDetalle CD ON C.id = CD.id_carrito INNER JOIN Producto P ON CD.id_producto = P.codigo WHERE C.id = <id del carrito a hacer checkout> GROUP BY P.descripcion, P.Precio, P.codigo;

select C.id as IdCarrito from carrito C inner join Usuario U where Usuario = {usuarioArg} and C.id = MAX(c.id);

def añadir
    if carrito_disponible:
         insert del carrito    
         select del id del carrito y lo guarda a la variable global
         carrito_disponible = true
    insert detalle del carrito (registro a carritoDetalle {carrito_id}

ELIMINAR DE CARRITO:
delete from carrito where id = {carrito_id}
select 
	P.Nombre as Producto,
    P.Descripcion as Descripcion,
    CD.cantidad as Cantidad,
	P.Precio*CD.cantidad as "Precio"
from Usuario U 
	inner join carrito C 
		on U.idUsuario = C.usuario
	inner join carritoDetalle CD
		on C.id = CD.id_carrito
	inner join Producto P
		on CD.id_producto = P.idProducto
group by P.idProducto
where C.id == {carrito_id};