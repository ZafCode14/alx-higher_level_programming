-- Lists all genres from "hbtn_0_tvshows"
-- displays the number of shows linked to each
SELECT tv_genres.name AS genre,
COUNT(*) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres AS tsg
ON tv_genres.id = tsg.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
