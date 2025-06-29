CREATE DATABASE IF NOT EXISTS dned;
USE dned;

-- Tabla: period
CREATE TABLE IF NOT EXISTS period (
    cod_period CHAR(50) PRIMARY KEY,
    initial_date DATE,
    final_date DATE,
    description VARCHAR(255)
);

-- Tabla: user_workspace
CREATE TABLE IF NOT EXISTS user_workspace (
    user_workspace_id CHAR(50) PRIMARY KEY,
    space VARCHAR(100),
    last_connection DATETIME,
    active BOOLEAN
);

-- Tabla: user_unal
CREATE TABLE IF NOT EXISTS user_unal (
    email_unal VARCHAR(100) PRIMARY KEY,
    document VARCHAR(50),
    name VARCHAR(100),
    lastname VARCHAR(100),
    full_name VARCHAR(200),
    gender VARCHAR(10),
    birth_date DATE,
    UNIQUE (document)
);

-- Tabla: user_workspace_associate
CREATE TABLE IF NOT EXISTS user_workspace_associate (
    email_unal VARCHAR(100),
    cod_unit CHAR(50),
    cod_period CHAR(50),
    FOREIGN KEY (email_unal) REFERENCES user_unal(email_unal),
    FOREIGN KEY (cod_period) REFERENCES period(cod_period)
);

-- Tabla: unit_unal
CREATE TABLE IF NOT EXISTS unit_unal (
    cod_unit CHAR(50) PRIMARY KEY,
    cod_facultad CHAR(50),
    name VARCHAR(100),
    description TEXT,
    type_unit VARCHAR(50)
);

-- Tabla: user_unit_associate
CREATE TABLE IF NOT EXISTS user_unit_associate (
    email_unal VARCHAR(100),
    cod_unit CHAR(50),
    cod_period CHAR(50),
    FOREIGN KEY (email_unal) REFERENCES user_unal(email_unal),
    FOREIGN KEY (cod_unit) REFERENCES unit_unal(cod_unit),
    FOREIGN KEY (cod_period) REFERENCES period(cod_period)
);

-- Tabla: school
CREATE TABLE IF NOT EXISTS school (
    cod_school CHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    type_facultad VARCHAR(50)
);

-- Tabla: unit_school_associate
CREATE TABLE IF NOT EXISTS unit_school_associate (
    cod_unit CHAR(50),
    cod_school CHAR(50),
    cod_period CHAR(50),
    FOREIGN KEY (cod_unit) REFERENCES unit_unal(cod_unit),
    FOREIGN KEY (cod_school) REFERENCES school(cod_school),
    FOREIGN KEY (cod_period) REFERENCES period(cod_period)
);

-- Tabla: headquarters
CREATE TABLE IF NOT EXISTS headquarters (
    cod_headquarters CHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    type_facultad VARCHAR(50)
);

-- Tabla: school_sede_associate
CREATE TABLE IF NOT EXISTS school_sede_associate (
    cod_school CHAR(50),
    cod_headquarters CHAR(50),
    cod_period CHAR(50),
    FOREIGN KEY (cod_school) REFERENCES school(cod_school),
    FOREIGN KEY (cod_headquarters) REFERENCES headquarters(cod_headquarters),
    FOREIGN KEY (cod_period) REFERENCES period(cod_period)
);

-- Tabla: type_user
CREATE TABLE IF NOT EXISTS type_user (
    type_user_id CHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

-- Tabla: type_user_association
CREATE TABLE IF NOT EXISTS type_user_association (
    email_unal VARCHAR(100),
    type_user_id CHAR(50),
    cod_period CHAR(50),
    PRIMARY KEY (email_unal, type_user_id, cod_period),
    FOREIGN KEY (email_unal) REFERENCES user_unal(email_unal),
    FOREIGN KEY (type_user_id) REFERENCES type_user(type_user_id),
    FOREIGN KEY (cod_period) REFERENCES period(cod_period)
);

-- Tabla central de correos emisores
CREATE TABLE IF NOT EXISTS email_sender (
    id CHAR(50) PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(100)
);

-- Asociación: email_sender con unidad
CREATE TABLE IF NOT EXISTS email_sender_unit (
    sender_id CHAR(50),
    cod_unit CHAR(50),
    PRIMARY KEY (sender_id, cod_unit),
    FOREIGN KEY (sender_id) REFERENCES email_sender(id),
    FOREIGN KEY (cod_unit) REFERENCES unit_unal(cod_unit)
);

-- Asociación: email_sender con escuela
CREATE TABLE IF NOT EXISTS email_sender_school (
    sender_id CHAR(50),
    cod_school CHAR(50),
    PRIMARY KEY (sender_id, cod_school),
    FOREIGN KEY (sender_id) REFERENCES email_sender(id),
    FOREIGN KEY (cod_school) REFERENCES school(cod_school)
);

-- Asociación: email_sender con sede
CREATE TABLE IF NOT EXISTS email_sender_headquarters (
    sender_id CHAR(50),
    cod_headquarters CHAR(50),
    PRIMARY KEY (sender_id, cod_headquarters),
    FOREIGN KEY (sender_id) REFERENCES email_sender(id),
    FOREIGN KEY (cod_headquarters) REFERENCES headquarters(cod_headquarters)
);

