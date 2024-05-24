-- a script that uses the hbtn_0d_tvshows database
SELECT a.name
FROM tv_genres a
LEFT JOIN tv_show_genres b
ON a.id = b.genre_id
LEFT JOIN tv_shows c
ON b.show_id = c.id
WHERE c.title = 'Dexter'
ORDER BY a.name
