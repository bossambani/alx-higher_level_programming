-- Select with 2 LEFT JOIN return NULL
-- Execute: cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT a.title, c.name
FROM tv_shows a
LEFT JOIN tv_show_genres b
ON a.id = b.show_id
LEFT JOIN tv_genres c
ON b.genre_id = c.id
ORDER BY 1,2 ASC;
