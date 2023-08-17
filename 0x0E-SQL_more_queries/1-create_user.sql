-- Create a new user on the MySQL server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all priveleges to the new user
GRANT ALL
   ON *.*
   TO 'user_0d_1'@'localhost'
