-- Create a database 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create a table 'states' in 'hbtn_0d_usa' database
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
