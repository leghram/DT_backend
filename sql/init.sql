-- Crear la tabla 'users'
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    username VARCHAR(100) NOT NULL,
    hash_password VARCHAR(5000) NOT NULL
);
