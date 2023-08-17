-- Create a database 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create a table 'cities'
CREATE TABLE hbtn_0d_usa.cities (
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
