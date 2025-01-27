
create database sistema_alquiler;

use sistema_alquiler;

CREATE TABLE usuario(id int  auto_increment primary key, user varchar(20), password varchar(80));

CREATE TABLE casa (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nombre VARCHAR(50), 
    direccion VARCHAR(50),
    cantidad_apartamentos INT
);

CREATE TABLE tipo_apartamento (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nombre VARCHAR(50) NOT NULL, 
    descripcion VARCHAR(200)
);

CREATE TABLE apartamento (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nombre VARCHAR(50),
    casa_id INT,
    tipo_apartamento_id INT,
    FOREIGN KEY(casa_id) REFERENCES casa(id),
    FOREIGN KEY(tipo_apartamento_id) REFERENCES tipo_apartamento(id)
);

CREATE TABLE inquilino (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(60),
    apellidos VARCHAR(60),
    cedula INT,
    telefono VARCHAR(12)
);

CREATE TABLE arriendo (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    estado VARCHAR(20), 
    precio DECIMAL(12,2), 
    fecha_inicio DATE, 
    fecha_terminacion DATE,
    apartamento_id INT, 
    inquilino_id INT,
    FOREIGN KEY(apartamento_id) REFERENCES apartamento(id),
    FOREIGN KEY(inquilino_id) REFERENCES inquilino(id)
);

CREATE TABLE tipo_servicios (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nombre VARCHAR(50) NOT NULL, 
    descripcion VARCHAR(200)
);

CREATE TABLE servicios (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    precio DECIMAL(12,2),
    tipo_servicios_id INT,
    arriendo_id INT,
    FOREIGN KEY(tipo_servicios_id) REFERENCES tipo_servicios(id),
    FOREIGN KEY(arriendo_id) REFERENCES arriendo(id)
);

CREATE TABLE historial_pagos (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    monto DECIMAL(12,2),
    fecha_pago DATE, 
    metodo_pago VARCHAR(50),
    arriendo_id INT,
    FOREIGN KEY(arriendo_id) REFERENCES arriendo(id)
);