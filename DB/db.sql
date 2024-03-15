create database Bocadito;
use Bocadito;
CREATE table cliente(
	id int not null auto_increment,
    nombre varchar(50),
    apellido varchar(50),
    direccion varchar(200),
    telefono int,
    primary key (id)
);