CREATE DATABASE db_agenda;

USE DATABASE db_agenda;

CREATE TABLE personas(
    id_persona int AUTOINCREMENT PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    primer_apellido varchar(50) NOT NULL,
    segundo_apellido varchar(50) NOT NULL,
    email varchar(100) NOT NULL,
    telefono varchar(10) NOT NULL,
);

INSERT INTO pensonas (nombre,primer_apellido,segundo_apellido,email,telefono)
VALUES 
("Dejah", "Thoris", "Barsoon","dejah@email.mr","1234567890"),
("John", "Carter", "Earth", "john@email.ea","2345678901");