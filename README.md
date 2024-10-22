# API Personas
Uso de FastAPI y SQLite3 para generar una API REST

## 1. Configurar codespace

1.1 Actualizar versiones de librerias y paquetes instalables

````shell
$ sudo apt-get update
````

1.2 Instalar MariaDB


````shell
$ sudo apt-get install mariadb-server -y
````

1.3 Detener el servidor

````shell
$ sudo /etc/init.d/mysql stop
````

1.4 Iniciar el servidor

````shell
$ sudo mysqld_safe --skip-grant-tables &
````

1.5 Conectando con el servidor MySQL

````shell
$ mysql -u root
````

1.6 Salir de la MariaDB

````shell
MariaDB [(none)]> exit;
````

## 2. Script para crear la base de datos

2.1 Diccionario de datos de la tabla **personas**.

|Atributos|Campo|Tipo de dato|Descripción|
| -- | -- | -- | -- |
| PK | id_persona | int | Identificador de la persona |
| - | nombre | varchar(50) | Nombre de la persona |
| - | primer_apellido | varchar(50) | Primer apellido de la persona |
| - | segundo_apellido | varchar (50) | Segundo apellido de la persona |
| - | email | varchar(100) |  Email de la persona |
| - | telefono | varchar(10) | Teléfono de la persona |

2.2 Script para crear la base de datos

* Crear la base de datos **db_agenda**.
* Crear la tabla **personas**.
* Insertar 2 registros en la tabla **personas**.

````sql
CREATE DATABASE db_agenda;

USE  db_agenda;

CREATE TABLE personas(
    id_persona int AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    primer_apellido varchar(50) NOT NULL,
    segundo_apellido varchar(50) NOT NULL,
    email varchar(100) NOT NULL,
    telefono varchar(10) NOT NULL
);

INSERT INTO personas (nombre,primer_apellido,segundo_apellido,email,telefono)
VALUES 
("Dejah", "Thoris", "Barsoon","dejah@email.com","1234567890"),
("John", "Carter", "Earth", "john@email.com","2345678901");

SELECT * FROM personas;
````

2.3 Crear la base de datos desde MariaDB shell

````shell
MariaDB [(none)]> source db_agenda.sql
````
