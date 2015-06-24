--> Drop All Tables
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS categories;
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
INSERT INTO users (username, pw_hash, first_name, last_name, email)
VALUES ('mangulo',
        '$2a$12$qjHLGwqTxGQqoF8py0WEEOB.GX3bKsjYIRb5M1/buvBJVdtDUKiwu',
        'Miguel',
        'Angulo',
        'maangulo12@gmail.com');

--> Projects Table
CREATE TABLE projects (
  project_id SERIAL,
  project_name VARCHAR(50) NOT NULL,
  project_type VARCHAR(30) NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (project_id),
  FOREIGN KEY (user_id) REFERENCES users (user_id)
);
INSERT INTO projects (project_name, project_type, user_id)
VALUES ('Canyon Lake House', 'UBuildIt', 1);

--> Categories Table
CREATE TABLE categories (
  category_id SERIAL,
  category_name VARCHAR(50) NOT NULL,
  project_id INT NOT NULL,
  PRIMARY KEY (category_id),
  FOREIGN KEY (project_id) REFERENCES projects (project_id)
);

--> Items Table
CREATE TABLE items (
  item_id SERIAL,
  item_name VARCHAR(50) NOT NULL,
  description VARCHAR(80) NOT NULL,
  budget DECIMAL NOT NULL,
  actual DECIMAL NOT NULL,
  notes VARCHAR(80) NOT NULL,
  category_id INT NOT NULL,
  PRIMARY KEY (item_id),
  FOREIGN KEY (category_id) REFERENCES categories (category_id)
);
