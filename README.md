# API Personas
Uso de FastAPI y SQLite3 para generar una API REST

## 1. Configurar codespace

1.1 Actualizar versiones de librerias y paquetes instalables

````shell
sudo apt-get update
````

1.2 Instalar MySQL

````shell
sudo apt-get install mysql-server -y
````

1.3 Conectando con el servidor MySQL

````shell
sudo mysql -u root
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
* Insertar 3 registros en la tabla **personas**.

````sql
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
````
