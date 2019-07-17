-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- SQL query that lists tv shows with a genre
SELECT tv_shows.title as title, tv_show_genres.genre_id as genre_id
FROM tv_shows INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id ASC;
