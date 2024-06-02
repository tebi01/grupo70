### Creación del repositorio. IGNORAR ESTE ARCHIVO

Este archivo es un archivo de texto plano que se creó automáticamente al crear el repositorio. No tiene ninguna función en el proyecto, por lo que puede ser eliminado sin problemas.

# cldeldes.csv: datos cliente | datos delivery | datos despacho
# columnas: clientenombre;clienteemail;clientetelefono;clienteclave;deliverynombre;deliveryvigente;deliverytelefono;deliverytiempo;deliverypreciounitario;deliverypreciomensual;deliveryprecioanual;despachadornombre;despachadortelefono
# Cliente(id, nombre, mail, telefono, clave). primeras cuatro columnas.
# Delivery(id, nombre, vigencia, telefono, tiempo, precio_unitario, precio_mensual, precio_anual)
# Despachador (id, nombre, telefono)
# error en la línea 65. salto de línea entre O y Ryan. Único nombre que tiene comillas al principio.

# restaurantes.csv 
# columnas: "nombre";"vigente";"estilo";"repartomin";"sucursal";"direccion";"telefono";"area"
# Restaurante(id, nombre, vigente, estilo, repartomin)
# Sucursal(id, direccion, comuna, telefono, id_restaurante)
# los nombres de las sucursales calzan CASI siempre con las palabras que están en la dirección entre la primera y la última (usualmente Av. o Calle, y al final suele haber un número) Ej: direccion = "Av. Las Parcelas 1234, Macul, Santiago" -> sucursal = "Las Parcelas". hay una excepción que hemos encontrado: "Av. San José María Escrivá de Balaguer 5970, Vitacura, Santiago" -> "Escriva de Balaguer"
# el área es igual a la comuna. también siempre parten con un espacio. en la dirección siempre es el segundo elemento al separar por comas (a veces hay tres; sigue siendo el segundo). Ej: direccion = "Calle Padre Mariano 789, La Reina, Santiago" -> area = " La Reina"
# excepción: hay un ejemplo que no es una comuna. "Santiago Centro" podemos convertirlo en "Santiago".

# Pedidos.csv
# columnas: id;cliente;delivery;despachador;plato;fecha;hora;estado
# Pedido(id, cliente, delivery, desspachador, fecha, hora, estado)
# Pedido_t
# El atributo platos son los id de los platos solicitados en ese pedido separados por espacio. Se podrían separar este atributo de la tabla pedidos y hacer una tabla pedido - plato (asociación)

# suscripciones.csv
# columnas: email;nombre;estado;ultimopago;fecha;ciclo
# Suscripcion(id, id_usuario, id_empresa, estado, ultimopago, fecha, ciclo)
# las vigentes tienen mayúscula, capaz que sería mejor cambiar "Vigente" por "vigente". 

# platos.csv
# columnas: id;nombre;descripcion;disponibilidad;estilo;restriccion;ingredientes;porciones;precio;tiempo;restaurant;repartomin;vigente
# nombre -> descripcion, estilo, restriccion, ingredientes
# restaurant -> repartomin, vigente. repartomin y vigente es la misma info de restaurantes.csv
# separar ingredientes en una nueva relación
# Plato(id, nombre, descripcion, estilo, restriccion, ingredientes)
# PlatoEnRestaurante(id_plato, id_restaurante, disponibilidad, porciones, precio, tiempo, disponibilidad)

EotalP 

# calificacion.csv
# columnas: "pedido";"resdel";"cliente"

