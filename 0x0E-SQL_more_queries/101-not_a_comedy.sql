-- List all the shows which are not comedies from the database
SELECT title
  FROM tv_shows
 WHERE title NOT IN
	   (SELECT tv_shows.title
		  FROM tv_shows
			   JOIN tv_show_genres
			   JOIN tv_genres
			   ON tv_shows.id = tv_show_genres.show_id
				  AND tv_genres.id = tv_show_genres.genre_id
		 WHERE tv_genres.name = 'Comedy')
 ORDER BY title ASC
