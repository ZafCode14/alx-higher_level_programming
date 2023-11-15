-- Lists all shows from "hbtn_0d_tvshows_rate"
SELECT tv_shows.title, SUM(tsr.rate) AS rating
FROM tv_shows
INNER JOIN tv_show_ratings AS tsr
ON tv_shows.id = tsr.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;
