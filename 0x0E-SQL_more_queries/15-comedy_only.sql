-- List all the comedy shows
SELECT tv_shows.title
  FROM tv_shows
	   INNER JOIN tv_show_genres
	   INNER JOIN tv_genres
	   ON tv_shows.id = tv_show_genres.show_id
		  AND tv_genres.id = tv_show_genres.genre_id
 WHERE tv_genres.name = 'Comedy'
 ORDER BY tv_shows.title ASC
