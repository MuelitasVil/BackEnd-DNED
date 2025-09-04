DROP DATABASE IF EXISTS dned;
CREATE DATABASE dned;
USE dned;

-- Tabla: period
DROP TABLE IF EXISTS period;
CREATE TABLE period (
    cod_period CHAR(50) PRIMARY KEY,
    initial_date DATE,
    final_date DATE,
    description VARCHAR(255)
);

-- Tabla: user_workspace
DROP TABLE IF EXISTS user_workspace;
CREATE TABLE user_workspace (
    user_workspace_id CHAR(50) PRIMARY KEY,
    space VARCHAR(100),
    last_connection DATETIME,
    active BOOLEAN
);

-- Tabla: user_unal
DROP TABLE IF EXISTS user_unal;
CREATE TABLE user_unal (
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
DROP TABLE IF EXISTS user_workspace_associate;
CREATE TABLE user_workspace_associate (
    email_unal VARCHAR(100),
    user_workspace_id CHAR(50),
    cod_period CHAR(50),
    FOREIGN KEY (email_unal) REFERENCES user_unal(email_unal),
    FOREIGN KEY (cod_period) REFERENCES period(cod_period)
);

-- Tabla: unit_unal
DROP TABLE IF EXISTS unit_unal;
CREATE TABLE unit_unal (
    cod_unit CHAR(50) PRIMARY KEY,
    email VARCHAR(100),
    name VARCHAR(100),
    description TEXT,
    type_unit VARCHAR(50)
);

-- Tabla: user_unit_associate
DROP TABLE IF EXISTS user_unit_associate;
CREATE TABLE user_unit_associate (
    email_unal VARCHAR(100),
    cod_unit CHAR(50),
    cod_period CHAR(50),
    FOREIGN KEY (email_unal) REFERENCES user_unal(email_unal),
    FOREIGN KEY (cod_unit) REFERENCES unit_unal(cod_unit),
    FOREIGN KEY (cod_period) REFERENCES period(cod_period)
);

-- Tabla: school
DROP TABLE IF EXISTS school;
CREATE TABLE school (
    cod_school CHAR(50) PRIMARY KEY,
    email VARCHAR(100),
    name VARCHAR(100),
    description TEXT,
    type_facultad VARCHAR(50)
);

-- Tabla: unit_school_associate
DROP TABLE IF EXISTS unit_school_associate;
CREATE TABLE unit_school_associate (
    cod_unit CHAR(50),
    cod_school CHAR(50),
    cod_period CHAR(50),
    FOREIGN KEY (cod_unit) REFERENCES unit_unal(cod_unit),
    FOREIGN KEY (cod_school) REFERENCES school(cod_school),
    FOREIGN KEY (cod_period) REFERENCES period(cod_period)
);

-- Tabla: headquarters
DROP TABLE IF EXISTS headquarters;
CREATE TABLE headquarters (
    cod_headquarters CHAR(50) PRIMARY KEY,
    email VARCHAR(100),
    name VARCHAR(100),
    description TEXT,
    type_facultad VARCHAR(50)
);

-- Tabla: school_headquarters_associate
DROP TABLE IF EXISTS school_headquarters_associate;
CREATE TABLE school_headquarters_associate (
    cod_school CHAR(50),
    cod_headquarters CHAR(50),
    cod_period CHAR(50),
    FOREIGN KEY (cod_school) REFERENCES school(cod_school),
    FOREIGN KEY (cod_headquarters) REFERENCES headquarters(cod_headquarters),
    FOREIGN KEY (cod_period) REFERENCES period(cod_period)
);

-- Tabla: type_user
DROP TABLE IF EXISTS type_user;
CREATE TABLE type_user (
    type_user_id CHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

-- Tabla: type_user_association
DROP TABLE IF EXISTS type_user_association;
CREATE TABLE type_user_association (
    email_unal VARCHAR(100),
    type_user_id CHAR(50),
    cod_period CHAR(50),
    PRIMARY KEY (email_unal, type_user_id, cod_period),
    FOREIGN KEY (email_unal) REFERENCES user_unal(email_unal),
    FOREIGN KEY (type_user_id) REFERENCES type_user(type_user_id),
    FOREIGN KEY (cod_period) REFERENCES period(cod_period)
);

-- Tabla central de correos emisores
DROP TABLE IF EXISTS email_sender;
CREATE TABLE email_sender (
    id CHAR(50) PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(100)
);

-- Asociación: email_sender con unidad
DROP TABLE IF EXISTS email_sender_unit;
CREATE TABLE email_sender_unit (
    sender_id CHAR(50),
    cod_unit CHAR(50),
    PRIMARY KEY (sender_id, cod_unit),
    FOREIGN KEY (sender_id) REFERENCES email_sender(id),
    FOREIGN KEY (cod_unit) REFERENCES unit_unal(cod_unit)
);

-- Asociación: email_sender con escuela
DROP TABLE IF EXISTS email_sender_school;
CREATE TABLE email_sender_school (
    sender_id CHAR(50),
    cod_school CHAR(50),
    PRIMARY KEY (sender_id, cod_school),
    FOREIGN KEY (sender_id) REFERENCES email_sender(id),
    FOREIGN KEY (cod_school) REFERENCES school(cod_school)
);

-- Asociación: email_sender con sede
DROP TABLE IF EXISTS email_sender_headquarters;
CREATE TABLE email_sender_headquarters (
    sender_id CHAR(50),
    cod_headquarters CHAR(50),
    PRIMARY KEY (sender_id, cod_headquarters),
    FOREIGN KEY (sender_id) REFERENCES email_sender(id),
    FOREIGN KEY (cod_headquarters) REFERENCES headquarters(cod_headquarters)
);

-- Auth tables : 
DROP TABLE IF EXISTS system_user;
CREATE TABLE system_user (
    email VARCHAR(100) PRIMARY KEY,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    hashed_password TEXT NOT NULL,
    state BOOLEAN DEFAULT TRUE,
    salt VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS token;
CREATE TABLE token (
    jwt_token VARCHAR(512) PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (email) REFERENCES system_user(email)
);
