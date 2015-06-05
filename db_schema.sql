--> Drop All Tables
DROP TABLE IF EXISTS invoices;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS users;

--> Users Table
CREATE TABLE users (
  user_id SERIAL,
  username VARCHAR(25) NOT NULL UNIQUE,
  pw_hash VARCHAR(60) NOT NULL,
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30) NOT NULL,
  email VARCHAR(50) NOT NULL UNIQUE,
  PRIMARY KEY (user_id)
);

--> Inserting into Users Table
INSERT INTO users (username, pw_hash, first_name, last_name, email)
VALUES ('mangulo',
        '$2a$12$qjHLGwqTxGQqoF8py0WEEOB.GX3bKsjYIRb5M1/buvBJVdtDUKiwu',
        'Miguel',
        'Angulo',
        'maangulo12@gmail.com');
