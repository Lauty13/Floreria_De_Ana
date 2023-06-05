create database floreria;
\c floreria

create table cliente (
    id serial,
    nombre varchar(25),
    apellido varchar(25),
    nro_contacto numeric(15),
    dni numeric(8),
    constraint pk_cliente primary key (id)
);

create table sucursal (
    id serial,
    direccion varchar(50),
    nombre varchar(25),
    constraint pk_sucursal primary key (id)
);

-- insumo se refiere a por ejemplo las flores individuales para un ramo
create table insumo
(nombre varchar (20),
constraint pk_insumo primary key(nombre)
);

create table detalle_producto(
    id serial,
    cantidad_necesaria numeric(10),
    insumo varchar(15),
    constraint pk_detalle_producto primary key(id),
    constraint fk_detalle_prod_insumo foreign key (insumo) references insumo(nombre)
);

--ramo, flores, corona, libre(lo que el cliente quiera)
create table producto
(nombre varchar(50),
descripcion text,
precio_unitario int,
detalle_producto int,
constraint pk_producto primary key(nombre),
constraint fk_producto_insumo foreign key (detalle_producto) references detalle_producto(id)
);

create table detalle_venta
(id serial,
cantidad_producto int,
producto varchar(50),
constraint pk_detalle_venta primary key(id),
constraint fk_detalle_producto foreign key (producto) references producto(nombre)
);

create table estado_venta
(id serial,
nombre varchar(30),
constraint pk_estado_venta primary key (id));

create table venta
(id serial,
fecha_hora timestamp,
sucursal integer,
cliente integer,
detalle_venta integer,
estado_venta integer,
constraint pk_venta primary key(id),
constraint fk_venta_cliente foreign key (cliente) references cliente(id),
constraint fk_venta_detalle foreign key (detalle_venta) references detalle_venta(id),
constraint fk_venta_estado foreign key (estado_venta) references estado_venta(id)
);

