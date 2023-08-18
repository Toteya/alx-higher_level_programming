-- List all genres not linked to the show Dexter from the database
SELECT name
  FROM tv_genres
 WHERE name NOT IN
		(SELECT tv_genres.name
		   FROM tv_genres
				JOIN tv_show_genres
				JOIN tv_shows
				ON tv_genres.id = tv_show_genres.genre_id
				   AND tv_shows.id = tv_show_genres.show_id
		  WHERE tv_shows.title = 'Dexter')
 ORDER BY tv_genres.name ASC
