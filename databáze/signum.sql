-- Vytvoření databáze
CREATE DATABASE IF NOT EXISTS client_system;
USE client_system;

-- Tabulka CLIENTS
CREATE TABLE CLIENTS (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(40) NOT NULL,
    lastname VARCHAR(60) NOT NULL,
    birthdate DATE NOT NULL,
    street VARCHAR(40) NOT NULL,
    housenum VARCHAR(10),
    postal VARCHAR(5),
    city VARCHAR(40),
    username VARCHAR(20) NOT NULL,
    passwd VARCHAR(128) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(20)
);

-- Tabulka CERTIFICATES
CREATE TABLE CERTIFICATES (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    clients_id INT UNSIGNED,
    certifkey VARCHAR(16) NOT NULL UNIQUE,
    CONSTRAINT fk_client
        FOREIGN KEY (clients_id) 
        REFERENCES CLIENTS(id)
        ON DELETE CASCADE
);

-- Vložení fiktivních dat do CLIENTS
INSERT INTO CLIENTS (firstname, lastname, birthdate, street, housenum, postal, city, username, passwd, email, phone)
VALUES 
('Jan', 'Novák', '1990-05-15', 'Dlouhá', '125', '11000', 'Praha', 'jnovak', 'hash_hesla_123', 'jan.novak@example.cz', '+420123456789'),
('Marie', 'Svobodová', '1985-11-02', 'Nádražní', '14', '60200', 'Brno', 'msvoboda', 'hash_hesla_456', 'marie@seznam.cz', '+420987654321'),
('Petr', 'Černý', '1998-02-28', 'Veselá', '9', '30100', 'Plzeň', 'pcerny', 'hash_hesla_789', 'cerny.p@gmail.com', '777111222');

-- Vložení fiktivních dat do CERTIFICATES
INSERT INTO CERTIFICATES (clients_id, certifkey)
VALUES 
(1, 'ABC123XYZ4567890'),
(1, 'CERT999888777666'),
(2, 'KEY0001112223334');
