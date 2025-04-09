-- models/genre_trends.sql

SELECT
    Genre,
    COUNT(*) AS total_songs,
    SUM(`Streams`) AS total_streams,
    ROUND(AVG(`Daily Streams`), 2) AS avg_daily_streams,
FROM `de-project-2025-455709`.`music`.`raw_music_streams`
GROUP BY Genre
ORDER BY total_songs DESC