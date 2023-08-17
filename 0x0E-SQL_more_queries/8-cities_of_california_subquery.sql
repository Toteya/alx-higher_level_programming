-- List all the cities of California in the database 'hbtn_0d_usa'
SELECT cities.id, states.id, cities.name
  FROM cities, states
 WHERE cities.state_id = states.id;
