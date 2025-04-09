-- models/top_artists.sql

SELECT
    Artist,
    COUNT(DISTINCT Song) AS total_songs,
    SUM(Streams) AS total_streams,
    ROUND(AVG(`Peak Position`), 2) AS avg_peak_position,
    SUM(`Weeks on Chart`) AS total_weeks,
    ROUND(AVG(`TikTok Virality`), 2) AS avg_tiktok_virality
FROM `de-project-2025-455709`.`music`.`raw_music_streams`
GROUP BY Artist
ORDER BY total_streams DESC