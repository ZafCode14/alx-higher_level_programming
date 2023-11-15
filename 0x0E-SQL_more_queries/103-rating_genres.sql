-- Lists all genres in "hbtn_0d_tvshows_rate" by their rating
SELECT tv_genres.name, SUM(tsr.rate) AS rating
FROM tv_genres
INNER JOIN tv_show_genres AS tsg
ON tv_genres.id = tsg.genre_id
INNER JOIN tv_show_ratings AS tsr
ON tsg.show_id = tsr.show_id
GROUP BY tv_genres.id
ORDER BY rating DESC;
