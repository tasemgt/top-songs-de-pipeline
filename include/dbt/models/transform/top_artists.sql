-- models/top_artists.sql

SELECT
    Artist,
    COUNT(DISTINCT Song) AS total_songs,
    SUM(Streams) AS total_streams,
FROM {{ source('music', 'raw_music_streams') }}
GROUP BY Artist
ORDER BY total_streams DESC
LIMIT 10
