-- Se creo la base de datos
create database Bocadito;
-- Se especifica que base de datos se usa
use Bocadito;
-- Se creo la tabla clientes
CREATE table cliente(
	id int not null auto_increment,
    nombre varchar(50),
    apellido varchar(50),
    direccion varchar(200),
    telefono int,
    -- La llave primaria es el id
    primary key (id)
);
-- Se inserto el primer registro
INSERT INTO cliente (nombre, apellido, direccion, telefono) VALUES ('Carlos', 'Talavera', 'Nandsime', 57968298);
-- Muestra la tabla
SELECT * FROM cliente;
