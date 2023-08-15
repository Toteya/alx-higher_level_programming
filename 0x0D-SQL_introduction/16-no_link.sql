-- List all the records of the table second_table except those without
-- a name value
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
