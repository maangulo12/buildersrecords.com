--> Drop All Tables
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

--> Projects Table
CREATE TABLE projects (
  project_id SERIAL,
  project_name VARCHAR(50) NOT NULL,
  project_type VARCHAR(30) NOT NULL,
  address VARCHAR(50) NOT NULL,
  city VARCHAR(40) NOT NULL,
  state VARCHAR(40) NOT NULL,
  zipcode VARCHAR(10) NOT NULL,
  project_cost DECIMAL NOT NULL,
  project_start_date DATE NOT NULL,
  project_end_date DATE NOT NULL,
  loan_question BOOLEAN NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (project_id),
  FOREIGN KEY (user_id) REFERENCES users (user_id)
);

INSERT INTO projects (project_name,
                      project_type,
                      address,
                      city,
                      state,
                      zipcode,
                      project_cost,
                      project_start_date,
                      project_end_date,
                      loan_question,
                      user_id)
VALUES ('Canyon Lake House',
        'UBuildIt - New Home',
        '251 Wizard Way',
        'Spring Branch',
        'TX',
        '78070',
        360000,
        '01/01/2015',
        '01/01/2016',
        'yes',
        1);
