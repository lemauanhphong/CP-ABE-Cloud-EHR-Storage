CREATE DATABASE authority_server;

USE authority_server;

CREATE TABLE
  users (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL,
    permission INT DEFAULT 0 NOT NULL,
    UNIQUE (username),
    PRIMARY KEY (id)
  );

INSERT INTO
  users (username, password, role)
VALUES
  ("admin", "password", "admin") -- admin account
