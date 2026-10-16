-- 1. Crear el esquema si no existe
CREATE SCHEMA IF NOT EXISTS stationary;

-- 2. Eliminar tablas previas si existen
DROP TABLE IF EXISTS stationary.products CASCADE;
DROP TABLE IF EXISTS stationary.employees CASCADE;
DROP TABLE IF EXISTS stationary.users CASCADE;

-- 3. Tabla de Empleados
CREATE TABLE stationary.employees (
    id_employee INT GENERATED ALWAYS AS IDENTITY, 
    name VARCHAR(100) NOT NULL,
    first_lastname VARCHAR(100) NOT NULL,
    second_lastname VARCHAR(100) NULL,
    rfc CHAR(18) NOT NULL,
    "user" VARCHAR(50) NOT NULL,
    "role" VARCHAR(20) NOT NULL DEFAULT 'Empleado',
    
    CONSTRAINT employee_pk PRIMARY KEY (id_employee),
    CONSTRAINT chk_employee_role CHECK ("role" IN ('Administrador', 'Empleado'))
);

-- 4. Tabla de Productos
CREATE TABLE stationary.products (
    id_product INT GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(150) NOT NULL,
    code VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    quantity INT NOT NULL,
    state VARCHAR(50) NOT NULL DEFAULT 'Disponible',
    
    CONSTRAINT product_pk PRIMARY KEY (id_product),
    CONSTRAINT chk_product_quantity CHECK (quantity >= 0),
    CONSTRAINT chk_product_state CHECK (state IN ('Disponible', 'Agotado'))
);

-- 5. Tabla de Inicio de Sesión (4 campos esenciales)
CREATE TABLE stationary.users (
    id_user INT GENERATED ALWAYS AS IDENTITY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    "role" VARCHAR(20) NOT NULL DEFAULT 'Empleado',
    
    CONSTRAINT user_pk PRIMARY KEY (id_user),
    CONSTRAINT chk_user_role CHECK ("role" IN ('Administrador', 'Empleado'))
);

-- 6. Comentarios descriptivos de las columnas
COMMENT ON COLUMN stationary.employees.name IS 'nombre del empleado';
COMMENT ON COLUMN stationary.employees.first_lastname IS 'primer apellido del empleado';
COMMENT ON COLUMN stationary.employees.second_lastname IS 'segundo apellido del empleado';
COMMENT ON COLUMN stationary.employees.rfc IS 'rfc o homoclave del empleado';
COMMENT ON COLUMN stationary.employees."user" IS 'nombre de usuario del empleado';
COMMENT ON COLUMN stationary.employees."role" IS 'rol del empleado (Administrador o Empleado)';

COMMENT ON COLUMN stationary.products.name IS 'nombre del producto';
COMMENT ON COLUMN stationary.products.code IS 'código identificador del producto';
COMMENT ON COLUMN stationary.products.description IS 'descripción detallada del producto';
COMMENT ON COLUMN stationary.products.quantity IS 'cantidad disponible en inventario';
COMMENT ON COLUMN stationary.products.state IS 'estado del producto (Disponible o Agotado)';

COMMENT ON COLUMN stationary.users.id_user IS 'identificador único de la cuenta';
COMMENT ON COLUMN stationary.users.username IS 'nombre de usuario para autenticación';
COMMENT ON COLUMN stationary.users.password IS 'contraseña de acceso al sistema';
COMMENT ON COLUMN stationary.users."role" IS 'rol asignado a la cuenta';

-- 7. Inserciones de Empleados
INSERT INTO stationary.employees (name, first_lastname, second_lastname, rfc, "user", "role") VALUES 
('Samantha Mabeth', 'Esquer', 'Lara', 'EULS060129HSUSRMA2', 'Samantha', 'Administrador'), 
('Claudio Tadeo', 'Lara', 'Aviles', 'KLLO230JNMAMN178L1', 'Claudio', 'Administrador'),
('Sergio Gael', 'Villanueva', 'Martínez', 'PELG060714HDGMRN08', 'Sergio', 'Administrador'), 
('Brandon', 'Martinez', 'Gamboa', 'MAGB070909HDGRMRA7', 'Brandon', 'Administrador'),
('Luis Alberto', 'Gómez', 'Pérez', 'GOPL950412HDF00001', 'Luis', 'Empleado'), 
('Ana María', 'Sánchez', 'Ruiz', 'SARA981123MDF00002', 'Ana', 'Empleado'),
('Carlos Javier', 'Díaz', 'Torres', 'DITC010203HDF00003', 'Carlos', 'Empleado');

-- 8. Inserciones de Productos
INSERT INTO stationary.products (name, code, description, quantity, state) VALUES
('Cuaderno', 'PRD-101', 'Cuaderno de raya forma francesa', 15, 'Disponible'),
('Lapiz', 'PRD-102', 'Lápiz grafito número 2', 0, 'Agotado'),
('Borrador', 'PRD-103', 'Borrador de migajón blanco', 25, 'Disponible');

-- 9. Inserciones de Usuarios para Login
INSERT INTO stationary.users (username, password, "role") VALUES
('Samantha', 'abcd', 'Administrador'),
('Claudio', '1234', 'Administrador'),
('Sergio', 'sergio123', 'Administrador'),
('Brandon', 'admin123', 'Administrador'),
('Oscar', 'pass123', 'Empleado');