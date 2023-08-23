-- A script that prepares a MYSQL server for the project
-- create a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
-- grant previleges
GRANT ALL PRIVILEGES
ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost';
