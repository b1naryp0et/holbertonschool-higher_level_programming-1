--List all shows that have one genre linked or more
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_shows_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
