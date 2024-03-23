-- Se crea la base de datos
create database Bocadito;
-- Decimos que DB vamos a usar
use Bocadito;
-- Mostramos la base de datos
show databases;
-- Creamos la tabla de clientes
create table clientes(
	id int not null auto_increment,
    cedula varchar(9) unique not null,
    primerNombre varchar(50),
    segundoNombre varchar(50),
    primerApellido varchar(50),
    usuario varchar(20),
    email varchar(50),
    contraseña varchar(16),
    primary key(id)
);