CREATE DATABASE cloud;

USE cloud;

CREATE TABLE
  health_records (
    id INT NOT NULL AUTO_INCREMENT,
    uid INT NOT NULL,
    creator INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    data LONGBLOB,
    PRIMARY KEY (id)
  );

CREATE TABLE
  person_profiles (
    id INT NOT NULL AUTO_INCREMENT,
    uid INT NOT NULL,
    creator INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    date_of_birth DATE,
    address VARCHAR(255) NOT NULL,
    data LONGBLOB,
    PRIMARY KEY (id)
  );

CREATE TABLE
  research (
    id INT NOT NULL AUTO_INCREMENT,
    uid INT NOT NULL,
    creator INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    data LONGBLOB,
    PRIMARY KEY (id)
  );

CREATE TABLE
  financials (
    id INT NOT NULL AUTO_INCREMENT,
    uid INT NOT NULL,
    creator INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    data LONGBLOB,
    PRIMARY KEY (id)
  );
