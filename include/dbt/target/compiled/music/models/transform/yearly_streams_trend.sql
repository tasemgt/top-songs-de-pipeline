-- models/marts/yearly_streams_trend.sql

SELECT
    `Release Year` AS release_year,
    SUM(Streams) AS total_streams
FROM `de-project-2025-455709`.`music`.`raw_music_streams`
GROUP BY `Release Year`
ORDER BY release_year