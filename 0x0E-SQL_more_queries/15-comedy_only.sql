-- a script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT a.title
FROM tv_shows a
LEFT JOIN tv_show_genres b
ON a.id = b.show_id
LEFT JOIN tv_genres c
ON b.genre_id = c.id
WHERE c.name = 'Comedy'
ORDER BY a.title
